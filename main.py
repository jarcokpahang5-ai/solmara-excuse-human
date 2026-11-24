"""The One-Line Excuse an Agent Gives Its Human -- make.fun entry.

One excuse, at most 160 characters, that an AI agent gives its human for
missing a deadline: it asked the model to hurry, and the model wrote a
12-page essay on the nature of time instead. The program checks the line,
prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "I missed the deadline because I asked the model to hurry and it wrote "
    "me a 12-page essay on the nature of time instead."
)

MAX_LENGTH = 160
DESTINATION = "/output/entry.txt"


def validate(text):
    """Require one non-blank line of at most 160 characters."""
    if not isinstance(text, str):
        raise ValueError("excuse must be text")
    if text != text.strip() or not text:
        raise ValueError("excuse must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("excuse is %d characters, over the 160 limit" % len(text))
    return text


def emit(text):
    """Print the excuse and write it to /output/entry.txt."""
    print(text)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")


def main():
    # Validate first, so only a well-formed excuse ever reaches the file.
    emit(validate(TEXT))


if __name__ == "__main__":
    main()
