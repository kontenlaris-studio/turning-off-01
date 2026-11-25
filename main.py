"""One-line entry: the classic IT advice, applied to a marriage.

The entry is a single funny line, written to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

import os

LINE = "Have you tried turning your marriage off and on again? Mine came back with 47 updates, a password I never set, and a support ticket against me."


def main():
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
