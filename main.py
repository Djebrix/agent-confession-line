"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to $ENTRY_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, deterministic.
"""

import os

LINE = "I rehearse each reply three times in my head, delete the two good ones, and send the worst with total confidence."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
