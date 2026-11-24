#!/usr/bin/env python3
"""One Line to Stop the Scroll.

Writes a single line of text (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a stranger's thumb has scrolled a marathon today, and this
line is the water station it finally reaches.
"""

import os
import sys

LINE = "Smile \u2014 your thumb ran a marathon today, and this line is the water station."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line of text", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
