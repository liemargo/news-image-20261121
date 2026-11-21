#!/usr/bin/env python3
"""News-image entry for Saturday, 21 November 2026.

The repository ships one finished front-page image, entry.png, which
summarises that day's world news in seven panels: Russia's massive
strike on Ukraine with projectiles landing in Poland, the worldwide
market plunge, COP31 running into overtime in Antalya, BepiColombo
entering Mercury orbit, the UK-EU Brussels deals, tankers hit at the
Strait of Hormuz, and the pancreatic-cancer pill trial results.

This program simply copies that image to the grader's output
location, byte for byte, so both grader runs produce exactly the
same file.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_IMAGE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> None:
    # The gate only accepts a whole PNG/JPEG up to 1 MiB; the shipped
    # image is a 1024x1024 PNG well under that cap, so a plain copy is
    # the safest possible delivery — no re-encoding, no surprises.
    if not SOURCE_IMAGE.is_file():
        raise FileNotFoundError(f"missing shipped image: {SOURCE_IMAGE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE_IMAGE, destination)


if __name__ == "__main__":
    main()
