"""Add a block of ES->EN translations into praxia-i18n.js, just before the
closing }; of the DICT (immediately after the 'Hecho en Madrid' entry, where
we already inserted the previous batch).

Each call appends a new section comment + entries.
"""
from pathlib import Path
import sys

# Anchor: insert AFTER the last colaboradores nav line we already added.
# We always add at the same place: just before the very first `};` after the
# DICT begins. The simplest reliable anchor is the line "    'Inscribirse': 'Apply now',"
# which is the LAST line of the previous batch.
ANCHOR = "    'Inscribirse': 'Apply now',\n"


def append_block(block):
    p = Path("praxia-i18n.js")
    s = p.read_text(encoding="utf-8")
    if ANCHOR not in s:
        print("ERROR: anchor not found")
        sys.exit(1)
    # Insert block AFTER the anchor line
    # We want every new block to be added right after the anchor, accumulating.
    # To avoid duplicating, ensure block doesn't already exist.
    if block.strip() and block.strip().splitlines()[0] in s:
        print("WARNING: first line of block already in file, skipping insert")
        return
    s = s.replace(ANCHOR, ANCHOR + block, 1)
    p.write_text(s, encoding="utf-8")
    print(f"Inserted block of {block.count(chr(10))} lines.")


if __name__ == "__main__":
    pass
