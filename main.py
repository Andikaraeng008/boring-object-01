"""Write the one-line review of the most boring everyday object.

Run from the repo root:  python3 main.py
Writes the review (119 characters) plus one trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt, byte-identically on every run.
"""

import os
import pathlib

LINE = "The lift music in this building has played the same four notes since 2009; even the buttons press themselves to escape."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = pathlib.Path(out_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
