
import { resolve } from 'node:path';
import fs from 'node:fs';

const markdownDir = resolve(__dirname, './markdown');

async function request(url: string, options = {}) {
  options = Object.assign({ method: "POST", "Referer": "https://www.baostock.com/mainContent?file=home.md", }, options);

  const response = await fetch(url, options);
  if (response.headers.get("content-type")?.includes("application/json")) {
    return await response.json();
  }
  return response.text();
}

/**
 * 获取菜单列表。响应格式为数组：
 ```json
 [{ "menuTitle": "平台介绍", "markdownFileName": "home.md", "comment": "tianyuan 增加..." }]
```
 * @returns
 */
async function getMenu() {
  let menu: {menuTitle: string; markdownFileName: string; }[] = await request("https://www.baostock.com/helpdocs/api/menu");
  // console.log(menu, menu.length);
  // 过滤部分菜单
  const filterMenu = ['goodArticle.md', 'default.md', 'modifyRecord.md'];
  menu = menu.filter(item => item.markdownFileName.endsWith('.md') && !filterMenu.some(d => d === item.markdownFileName));
  return menu;
}

async function getMarkdown(fileName: string) {
  let markdown: string = await request(`https://www.baostock.com/helpdocs/api/markdown/${fileName}`, {
    method: "POST",
  });

  markdown = markdown
    .replaceAll('https://www.baostock.com/mainContent?file=', '') // 文件引用链接清理
    .replace(/<style>[\s\S]*?<\/style>/g, '') // 移除 <style> 标签
    .replace(/([a-z0-9]+)\\_/g, '$1_')  // \_ 不必要的转义符
    .replace(/<a id=[^>]+><\/a>/g, '')   // 锚点
    .split('\n').map(line => line.trimEnd()).join('\n').trim()    // 每一行都 trim  End 一下
    .replace(/\n{3,}/g, '\n\n')         // 连续 3 行及以上换行符替换为 2 个换行符
  return markdown;
}

async function donwloadMarkdown() {
  if (!fs.existsSync(markdownDir)) fs.mkdirSync(markdownDir, { recursive: true });

  const menu = await getMenu();

  // 生成 index.md 文件
  const indexContent = ['# baostock 知识库目录\n'];

  for (const item of menu) {
    if (!item?.markdownFileName?.endsWith('.md')) continue;
    console.log('下载文件：', item.menuTitle, item.markdownFileName);
    const markdown = await getMarkdown(item.markdownFileName);

    fs.writeFileSync(resolve(markdownDir, item.markdownFileName), markdown);
    console.log(' > 文件已保存', item.markdownFileName);
    indexContent.push(`- [${item.menuTitle.replace(/^-+/, '')}](${item.markdownFileName})`);
  }

  fs.writeFileSync(resolve(markdownDir, 'index.md'), indexContent.join('\n'));

}

donwloadMarkdown();
