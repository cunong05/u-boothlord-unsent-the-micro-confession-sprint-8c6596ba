#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes the two-part micro-confession to /output/entry.txt and prints it.

Format (exactly two parts, no explanation after):
  1. A "To:" line naming who the message was meant for.
  2. The unsent message itself, one line, exactly as typed.
"""

# ENTRY is the two-part confession: line 1 is the addressee, line 2 is
# the unsent message. Nothing else is written to /output/entry.txt.

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
