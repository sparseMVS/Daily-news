#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path("/Users/zl/AMy/projects/amigos/file/资料汇总")
NEWS_DIR = ROOT / "每周新闻汇总"
README_PATH = ROOT / "README.md"
WEEKLY_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def extract_dates(text: str) -> list[str]:
    return re.findall(r"^## (\d{4}-\d{2}-\d{2})$", text, flags=re.MULTILINE)


def build_readme(files: list[Path]) -> str:
    lines = [
        "# 每周新闻汇总",
        "",
        "自动汇总的 AI 前沿技术新闻索引。",
        "",
        "## 最新周报",
        "",
    ]

    if not files:
        lines.extend(["暂无周报。", ""])
        return "\n".join(lines)

    latest = files[0]
    lines.append(f"- [{latest.name}](./每周新闻汇总/{latest.name})")
    lines.append("")
    lines.append("## 全部周报")
    lines.append("")

    for path in files:
        text = path.read_text(encoding="utf-8")
        dates = extract_dates(text)
        summary = f"包含 {len(dates)} 天内容"
        if dates:
            summary = f"包含 {dates[-1]} 至 {dates[0]} 的内容"
        lines.append(f"- [{path.name}](./每周新闻汇总/{path.name})：{summary}")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    files = sorted(
        [path for path in NEWS_DIR.glob("*.md") if WEEKLY_FILE_RE.match(path.name)],
        reverse=True,
    )
    README_PATH.write_text(build_readme(files), encoding="utf-8")


if __name__ == "__main__":
    main()
