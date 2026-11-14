"""Ship the bundled ramen photograph as the entry picture."""

import os
import shutil
from pathlib import Path


def _bundled_picture() -> Path:
    here = Path(__file__).resolve().parent
    return here / "entry.png"


def _destination_folder() -> Path:
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(wanted)


def main() -> None:
    source = _bundled_picture()
    target_dir = _destination_folder()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    # A plain byte copy with no re-encoding, so two runs write identical bytes.
    with source.open("rb") as incoming, target.open("wb") as outgoing:
        shutil.copyfileobj(incoming, outgoing, length=1 << 16)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("entry picture did not copy whole")


if __name__ == "__main__":
    main()
