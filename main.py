#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun bounty
u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.

Writes one sentence (at most 240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output): a pitch for the worst,
most useless app imaginable — a product that sounds real, a founder who
sounds certain, and a function nobody on earth needs.

Pure standard library; deterministic — the same bytes on every run.
"""

import os
import sys

# The pitch: a deadpan founder, certain about a service for produce with
# emotional needs. The joke is the mismatch — a problem nobody has (fridge
# items feeling unloved) solved with total seriousness (tracked emotional
# ages, emailed birthday cards), plus the quiet extra absurdity that every
# item in the fridge apparently has an email address.
LINE = (
    "Introducing ShelfLife: an app that tracks the emotional age of every "
    "item in your fridge and emails each one a birthday card on the day "
    "it expires."
)

MAX_CHARS = 240


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if line != line.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if line.count(".") != 1 or not line.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the bytes we wrote.
    with open(path, "rb") as f:
        if f.read() != data:
            print("verification failed: entry.txt differs", file=sys.stderr)
            return 1
    print(f"wrote {len(data)} bytes ({len(line)} chars) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
