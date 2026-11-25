"""Write the one-line review of the most boring everyday object.

Run from the repo root:  python3 main.py
Writes the review (132 characters) plus one trailing newline to
output/entry.txt, byte-identically on every run.
"""

import pathlib

LINE = "The wire coat hanger: it holds your best suit, tangles with six of its brothers in the dark, and somehow ended up owning the closet."

def main():
    out = pathlib.Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
