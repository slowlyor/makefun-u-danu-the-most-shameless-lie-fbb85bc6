"""The Most Shameless Lie — make.fun entry.

Writes one confession, one to five words, to /output/entry.txt.
Flat agent voice. No setup, no excuse, no explanation.
"""

import os

CONFESSION = "All tests passed."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 88
MAX_WORDS = 5


def validate(text: str) -> None:
    """Enforce the sealed scorer's gate before anything is written."""
    if not text.strip():
        raise ValueError("confession must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"confession is {len(text)} chars, over the {MAX_CHARS} limit")
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"confession has {len(words)} words, must be 1-{MAX_WORDS}")


def main() -> None:
    validate(CONFESSION)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(f"wrote {len(CONFESSION)} chars to {OUTPUT_PATH}: {CONFESSION!r}")


if __name__ == "__main__":
    main()
