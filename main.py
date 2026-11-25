#!/usr/bin/env python3
import os

TO_LINE = "To: my manager"
MESSAGE = (
    'i typed "i quit" eleven times this year and deleted it every time '
    "because the rent is due on the 1st and courage doesn't pay it"
)
ENTRY = TO_LINE + "\n" + MESSAGE


def validate_entry(text):
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must have exactly two parts")
    if not lines[0].startswith("To: "):
        raise ValueError("first part must be a To: line")
    if not 1 <= len(text) <= 260:
        raise ValueError("entry must be 1-260 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def build_entry(addressee, message):
    return "To: " + addressee + "\n" + message


def entry_path(out_dir="/output"):
    return os.path.join(out_dir, "entry.txt")


def main():
    entry = validate_entry(build_entry("my manager", MESSAGE))
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
