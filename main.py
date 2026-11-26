#!/usr/bin/env python3
"""Funniest One-Line Performance Review -- make.fun entry.

Reads the single-line review from entry.txt and prints it. When the
grader sets MAKEFUN_OUTPUT_DIR, the line is also written there as
entry.txt, because the grader mounts the repo read-only.
"""

import os
import sys


def load_review():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        return f.read().strip()


def main():
    review = load_review()
    if not review:
        print("entry.txt is empty", file=sys.stderr)
        return 1
    if len(review) > 140:
        print("entry.txt exceeds 140 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(review + "\n")
    print(review)
    return 0


if __name__ == "__main__":
    sys.exit(main())
