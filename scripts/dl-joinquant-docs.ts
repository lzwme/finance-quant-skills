/**
 * 从聚宽官方文档下载所有文档
 */

import * as path from 'node:path'
import * as fs from 'node:fs'
import TurndownService from 'turndown'
import { gfm } from 'turndown-plugin-gfm'
import { color } from '@lzwme/fe-utils'

async function getToekn() {
    const html = await fetch(`https://www.joinquant.com/help/api/help`).then(d => d.text())
    const token = html.match(/name:"token",value:"([a-zA-Z0-9]+)"/)?.[1]
    console.log('token:', token)
    return token
}

async function getContent(name = 'macroData', token?: string) {
    if (!token) token = await getToekn();
    const result = await fetch(`https://www.joinquant.com/help/api/getContent?name=${name}&token=${token}`, {
        "referrer": "https://www.joinquant.com/help/api/help"
    }).then(d => d.json());

    return result.data as string
}

/**
 * 聚宽 <article> 内是 Markdown 原文，页面靠 CSS(white-space) 保留换行。
 * Turndown 会按 HTML 规范折叠空白，导致 article 内的换行、列表缩进全部丢失，
 * 转换后所有内容被压成一行。因此先把 article 内容抽出单独转换，再用占位符回填。
 */
const articlePlaceholder = (id: number) => `JQARTICLEMDPLACEHOLDER${id}END`

/** 压缩多余空行（最多保留一个），代码块内的空行保持原样 */
function collapseBlankLines(md: string) {
    const lines: string[] = []
    let inFence = false
    for (const line of md.split('\n')) {
        if (/^\s*(```|~~~)/.test(line)) inFence = !inFence
        if (!inFence && !line && lines[lines.length - 1] === '') continue
        lines.push(line)
    }
    return lines.join('\n')
}

/** 解码 article 原文中的 HTML 实体（原本由 Turndown 的 DOM 解析自动完成） */
function decodeHtmlEntities(text: string) {
    const entities: Record<string, string> = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: '\u00a0' }
    return text.replace(/&(#(?:x[\da-f]+|\d+)|[a-z]+);/gi, (match, entity: string) => {
        if (entity.startsWith('#')) {
            const code = /^#x/i.test(entity)
                ? Number.parseInt(entity.slice(2), 16)
                : Number.parseInt(entity.slice(1), 10)
            return code >= 0 && code <= 0x10ffff ? String.fromCodePoint(code) : match
        }
        return entities[entity.toLowerCase()] ?? match
    })
}

function createTurndownService() {
    // 禁用自动转义，避免 run_abc 变成 run\_abc
    TurndownService.prototype.escape = (str: string) => str
    const turndownService = new TurndownService({
      headingStyle: 'atx',
      codeBlockStyle: 'fenced',
      emDelimiter: '*',
      bulletListMarker: '-',
      preformattedCode: true,
    });
    gfm(turndownService)
    return turndownService
}

/** 转换 <article> 内容：正文是 Markdown 原文，只需转换其中嵌入的 HTML 片段 */
function articleHtmlToMd(body: string, service: ReturnType<typeof createTurndownService>) {
    // 仅切出内嵌的 HTML 片段（代码块、链接、换行标签），其余原文保留换行与缩进
    const htmlSnippetRE = /(<pre\b[^>]*>[\s\S]*?<\/pre>|<a\b[^>]*>[\s\S]*?<\/a>|<br\s*\/?>)/gi
    const md = body.split(htmlSnippetRE).map((part, index) => {
        if (index % 2 === 0) return decodeHtmlEntities(part.replace(/\r\n?/g, '\n'))
        if (/^<br\b/i.test(part)) return '\n'
        const snippet = service.turndown(part).trim()
        return /^<pre\b/i.test(part) ? `\n\n${snippet}\n\n` : snippet
    }).join('')
    return collapseBlankLines(md).trim()
}

function htmlToMd(html: string) {
    const turndownService = createTurndownService()
    const articleMdList: string[] = []
    const preparedHtml = html.replace(/<article\b[^>]*>([\s\S]*?)<\/article>/gi, (_match, body: string) => {
        const id = articleMdList.push(articleHtmlToMd(body, turndownService)) - 1
        return `<article>${articlePlaceholder(id)}</article>`
    })

    let markdown = turndownService.turndown(preparedHtml)
    articleMdList.forEach((articleMd, id) => {
        markdown = markdown.replace(articlePlaceholder(id), () => articleMd)
    })

    markdown = collapseBlankLines(markdown
        // 将 ```python 替换为 ```python3
        .replace(/```python/g, '```py')
        .replace(/(\S*) +$/gm, '$1') // 去除行尾空格
        .replace(/^(-|\d+\.)\s{2,}/gm, '$1 ')) // 去除列表项前面多余的空格
    console.log(`转换成功！${html.length} -> ${markdown.length}`);
    return markdown.trim()
}

async function main() {
    const forceUpdate = process.env.FORCE_UPDATE === '1' || process.argv.slice(2).includes('--force-update')
    // https://www.joinquant.com/data
    // copy([...document.querySelectorAll('.data-dic a')].map(d => d.href.split('#name:')[1]).filter(Boolean))
    const jidList = new Set([
        'api',
        'faq',
        'factor',
    ])
    const dataIdList = new Set([
        "Stock",
        "plateData",
        "index",
        "macroData",
        "Future",
        "Option",
        "fund",
        "OTCfund",
        "technicalanalysis",
        "Alpha101",
        "Alpha191",
        "factor_values",
        "Public",
        "bond",
    ])

    const skillDir = './skills/joinquant-strategy'
    const localCacheDir = './skills/joinquant-strategy/local'
    const token = await getToekn()
    fs.mkdirSync(localCacheDir, { recursive: true })

    for (const id of [...jidList, ...dataIdList]) {
        // 下载保存的目录，除 jidList 中的外，其他的保存到 data 目录下
        const savedir = jidList.has(id) ? skillDir : path.join(skillDir, 'data');
        const htmlPath = path.join(localCacheDir, `${id}.html`)
        const filepath = path.join(savedir, `${id}.md`)
        if (fs.existsSync(filepath) && !forceUpdate) {
            console.log(`md文件已存在！${color.cyan(filepath)}`)
            continue
        }

        let htmlContent = ''
        if (fs.existsSync(htmlPath) && !forceUpdate) {
            htmlContent = fs.readFileSync(htmlPath, 'utf-8')
        } else {
            htmlContent = await getContent(id, token)
            if (!htmlContent?.length) {
                console.log(`${id} 获取内容失败！`)
                continue
            }
            fs.writeFileSync(htmlPath, htmlContent)
        }

        const mdContent = htmlToMd(htmlContent)
        fs.writeFileSync(filepath, mdContent)
        console.log(`${id} 文件保存成功！${color.green(filepath)}`)
    }
}

main()
