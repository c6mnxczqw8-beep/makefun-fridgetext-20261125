#!/usr/bin/env python3
"""Entry program for The 3AM Fridge Text make.fun bounty.

Writes one line (at most 140 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the text a smart fridge sends its owner at 3am, in the voice of
an appliance that has been awake all night, watching the
leftovers change.
"""

import os

TEXT = (
    "It's 3am. The leftovers from March have achieved "
    "consciousness, elected a leader, and are asking when "
    "you'll be home."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
