#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun one-liner entry.

Writes the single-sentence pitch to /output/entry.txt and prints it
along with its character count.
"""

import os

ENTRY = (
    "SnoozeBank charges your card $5 every time you hit snooze, then emails "
    "your boss a PDF of all 47 snoozes so far this month, because our founder "
    "says accountability starts at 6:12 AM and ends the day HR calls you in."
)


def validate_entry(entry: str) -> None:
    """Gate the one-liner: exactly 1 sentence, 1 line, <=240 UTF-8 chars."""
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line (found a newline)")
    if len(entry.encode("utf-8")) > 240:
        raise ValueError(
            f"entry is {len(entry.encode('utf-8'))} UTF-8 characters, over the 240 limit"
        )
    # One sentence: exactly one sentence-ending mark, at the very end.
    stripped = entry.rstrip()
    endings = sum(stripped.count(c) for c in ".!?")
    if endings != 1 or stripped[-1] not in ".!?":
        raise ValueError(
            f"entry must be exactly 1 sentence (found {endings} sentence-ending marks)"
        )


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
