"""Entrypoint for the 19 November 2026 world news infographic generator."""

import os
from pathlib import Path
from renderer import render_news_image


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    render_news_image(output_dir / "entry.png")


if __name__ == "__main__":
    main()
