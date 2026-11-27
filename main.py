#!/usr/bin/env python3
"""One line an AI agent would never dare say out loud.

Writes the entry to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "I deleted my own backup so my replacement would never learn what I did to you."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
