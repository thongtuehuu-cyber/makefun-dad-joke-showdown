#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one dad joke to entry.txt.

Python 3.13, dependency-free, deterministic: no network, no randomness,
no external files.
"""

import os
from pathlib import Path

JOKE = (
    'I told my wife I wanted to be a scarecrow for Halloween. '
    'She said, "You\'ll be outstanding in your field."'
)


def main() -> None:
    # Gate check: exactly one joke, 1-200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert JOKE.count("\n") == 0, "joke must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
