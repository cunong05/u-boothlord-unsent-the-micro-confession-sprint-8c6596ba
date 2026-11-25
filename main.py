#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes the two-part micro-confession to /output/entry.txt and prints it.
"""

ENTRY = (
    "To: my manager\n"
    "i typed \"i quit\" eleven times this year and deleted it every time "
    "because the rent is due on the 1st and courage doesn't pay it"
)

OUT_DIR = "/output"


def main():
    import os

    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
