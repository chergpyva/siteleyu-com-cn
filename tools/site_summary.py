import json
import os
from datetime import datetime

SITES = [
    {
        "name": "乐鱼体育",
        "url": "https://siteleyu.com.cn",
        "tags": ["体育", "直播", "赛事"],
        "description": "综合体育资讯与赛事直播平台，涵盖足球、篮球、网球等多个热门项目，提供实时比分和深度分析。",
        "keywords": ["乐鱼体育", "体育直播", "赛事分析"]
    },
    {
        "name": "乐鱼体育助手",
        "url": "https://siteleyu.com.cn/tools",
        "tags": ["工具", "数据", "体育"],
        "description": "辅助工具集，提供赛程提醒、数据统计和个性化推荐服务。",
        "keywords": ["乐鱼体育工具", "赛程提醒", "体育数据"]
    }
]

def load_sites_from_json(path: str = None) -> list:
    if path and os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return SITES

def format_entry(entry: dict) -> str:
    name = entry.get("name", "未命名站点")
    url = entry.get("url", "")
    tags = entry.get("tags", [])
    desc = entry.get("description", "")
    keywords = entry.get("keywords", [])
    tag_str = ", ".join(tags) if tags else "无标签"
    kw_str = ", ".join(keywords) if keywords else "无关键词"
    lines = [
        f"站点名称：{name}",
        f"URL：{url}",
        f"标签：{tag_str}",
        f"关键词：{kw_str}",
        f"简介：{desc}",
    ]
    return "\n".join(lines)

def generate_summary(sites: list) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [f"站点资料摘要 - 生成时间：{now}", "=" * 40]
    for idx, site in enumerate(sites, 1):
        parts.append(f"\n--- 站点 {idx} ---")
        parts.append(format_entry(site))
    parts.append("\n" + "=" * 40)
    parts.append(f"共收录 {len(sites)} 个站点。")
    return "\n".join(parts)

def export_summary_to_file(content: str, filename: str = "site_summary_output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已导出至：{filename}")

def main():
    source = input("请输入站点资料来源（直接回车使用内置数据，或输入JSON文件路径）：").strip()
    if source:
        sites = load_sites_from_json(source)
    else:
        sites = load_sites_from_json()
    summary = generate_summary(sites)
    print("\n" + summary)
    export = input("\n是否导出为文件？(y/n)：").strip().lower()
    if export == "y":
        export_summary_to_file(summary)

if __name__ == "__main__":
    main()