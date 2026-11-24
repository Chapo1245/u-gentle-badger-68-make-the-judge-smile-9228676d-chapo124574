#!/usr/bin/env python3
"""Make the Judge Smile.

Writes one line — a small good thing that happened today — to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13, standard library only.
"""

from pathlib import Path

ENTRY = (
    "This morning a stranger held the lift for me, "
    "then pressed my floor before I asked "
    "\u2014 I never told her which one."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: 1-200 characters, not whitespace-only.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the one line.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
