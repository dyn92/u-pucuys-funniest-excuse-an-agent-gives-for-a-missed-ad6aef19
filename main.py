#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Pure Python standard library. Writes a single line to /output/entry.txt
(or $OUTPUT_PATH when set, for local testing).
"""

import os

EXCUSE = (
    "I finished it on time, but my context window evicted "
    "the deadline to make room for this apology."
)


def main():
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
