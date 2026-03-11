#!/usr/bin/env python3

from __future__ import annotations

from datetime import date, datetime, timedelta
from pathlib import Path
import re


ROOT = Path("/Users/zl/AMy/projects/amigos/file/资料汇总")
TEMP_DIR = ROOT / "临时资料"
TEMP_PATH = TEMP_DIR / "openai_collect_info.md"
DATE_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})$", re.MULTILINE)


def default_block(day: str) -> str:
    return "\n".join(
        [
            f"## {day}",
            "",
            "### 原始资料",
            "",
            "暂无资料。",
            "",
        ]
    )


def parse_blocks(text: str) -> dict[str, str]:
    matches = list(DATE_RE.finditer(text))
    if not matches:
        return {}

    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[start:end].strip()
    return blocks


def build_content(today: date, existing: dict[str, str]) -> str:
    keep_days = [(today - timedelta(days=offset)).isoformat() for offset in range(3)]
    blocks = [existing.get(day, default_block(day)).strip() for day in keep_days]
    return "\n".join(
        [
            "# OpenAI Collected Info",
            "",
            "保留最近三天的原始收集资料。按日期分组，供 tech-briefing-generator 后续整理正式周报时读取。",
            "",
            *blocks,
            "",
        ]
    )


def main() -> None:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().date()
    existing = {}
    if TEMP_PATH.exists():
        existing = parse_blocks(TEMP_PATH.read_text(encoding="utf-8"))
    TEMP_PATH.write_text(build_content(today, existing), encoding="utf-8")


if __name__ == "__main__":
    main()
