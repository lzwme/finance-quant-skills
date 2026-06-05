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

function htmlToMd(html: string) {
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
    const markdown = turndownService.turndown(html)
    .replace(/(\S+) +$/gm, '$1') // 去除行尾空格
    .replace(/^-\s{2,}/gm, '- ') // 去除列表项前面多余的空格
    console.log(`转换成功！${html.length} -> ${markdown.length}`);
    return markdown.trim()
}

async function main() {
    const forceUpdate = process.env.FORCE_UPDATE === '1' || process.argv.slice(2).includes('--force-update')
    // https://www.joinquant.com/data
    // copy([...document.querySelectorAll('.data-dic a')].map(d => d.href.split('#name:')[1]).filter(Boolean))
    const contentIdList = [
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
        "bond"
    ]

    const savedir = './skills/joinquant-docs/data'
    const token = await getToekn()

    for (const id of contentIdList) {
        const htmlPath = path.join(savedir, `local/${id}.html`)
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
            fs.writeFileSync(path.join(savedir, `local/${id}.html`), htmlContent)
        }

        const mdContent = htmlToMd(htmlContent)
        fs.writeFileSync(filepath, mdContent)
        console.log(`${id} 文件保存成功！${color.green(filepath)}`)
    }
}

main()
