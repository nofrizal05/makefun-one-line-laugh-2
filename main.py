#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry for @nofrizal.

Writes one funny line to /output/entry.txt and prints it.
Python 3.13 standard library only.
"""

import os

LINE = "My Roomba joined a biker gang. Now it only comes home to charge and lie about where it's been."

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise ValueError("the line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("the line is longer than 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must be a single line")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the line, byte-identical every run.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
