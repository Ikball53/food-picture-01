"""Ship the bundled ramen photograph as the entry image.

The photograph sits beside this file as entry.png. This runner copies its
bytes unchanged into the output folder, so the judge sees the picture
exactly as it was made.
"""

import os
from pathlib import Path


def _photo_path() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def _target_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen)


def main() -> None:
    source = _photo_path()
    destination = _target_dir()
    destination.mkdir(parents=True, exist_ok=True)
    picture_bytes = source.read_bytes()
    written = destination / "entry.png"
    written.write_bytes(picture_bytes)
    # The copy must be exact: same bytes, same size, nothing dropped.
    if written.stat().st_size != len(picture_bytes):
        raise RuntimeError("entry image was not copied whole")


if __name__ == "__main__":
    main()
