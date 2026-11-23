#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for missing a spot to
/output/entry.txt. Python standard library only, no network.
"""

import os

LINE = (
    "My cliff sensor mistook the rug fringe for a canyon, "
    "my schedule has no rescue missions, and I was at 3% battery. "
    "The crumb stays \u2014 it has seniority now."
)


def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
