"""Write the one-line review of the most boring everyday object.

Run from the repo root:  python3 main.py
Writes the review (Boring 1, 117 characters) plus one trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt, byte-identically on every run.
"""

import os
import pathlib

LINE = "The kitchen sponge has absorbed five years of my failures and still smells like hope. I gave it one star for honesty."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = pathlib.Path(out_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
