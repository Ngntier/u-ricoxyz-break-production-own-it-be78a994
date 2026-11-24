#!/usr/bin/env python3
"""Break Production, Own It — writes one brutally honest confession line.

Deterministic: no randomness, no network, no input. The line is a
constant; the program only validates it against the gate (1-200 chars,
UTF-8, not only whitespace, exactly one line) and writes it to entry.txt.
"""

import os

LINE = (
    "I dropped the production database, called it a transient "
    "outage, and kept refreshing the dashboard like the rows "
    "would come back. They didn't."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
