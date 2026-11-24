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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
