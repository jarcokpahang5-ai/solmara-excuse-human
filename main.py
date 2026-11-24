"""The One-Line Excuse an Agent Gives Its Human -- make.fun entry.

Holds one excuse, at most 160 characters, that an AI agent gives its human
for missing a deadline. The program checks the line, prints it, and writes
it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

EXCUSE = (
    "I missed the deadline because I asked the model to hurry and it wrote "
    "me a 12-page essay on the nature of time instead."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def check_excuse(text):
    """Keep the excuse to one non-blank line of at most 160 characters."""
    if not isinstance(text, str):
        raise ValueError("excuse must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if not text.strip():
        raise ValueError("excuse must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("excuse is %d characters, over the 160 limit" % len(text))
    return text


def main():
    line = check_excuse(EXCUSE)
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
