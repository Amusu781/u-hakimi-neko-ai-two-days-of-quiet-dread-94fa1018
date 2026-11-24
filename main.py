#!/usr/bin/env python3
"""Write one code review comment to /output/entry.txt."""

import os

COMMENT = "LGTM. Clean diff, solid tests. In a year this will be legacy code, and so will I. Approving."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
MAX_CHARS = 140

if "\n" in COMMENT or not 1 <= len(COMMENT) <= MAX_CHARS:
    raise SystemExit("comment must be a single line of 1-140 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(COMMENT)
