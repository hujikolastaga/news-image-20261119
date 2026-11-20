"""Entrypoint for the 19 November 2026 world news infographic generator."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from renderer import render_news_image


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    render_news_image(output_dir / "entry.png")


if __name__ == "__main__":
    main()
