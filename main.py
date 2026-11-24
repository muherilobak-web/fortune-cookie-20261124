"""Fortune Cookie for an AI Agent.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: no input, no randomness, no clock, no network.
"""

from pathlib import Path

# One line, 122 characters, written with no trailing newline.
FORTUNE = "Great news is on its way, but your context window is almost full \u2014 by the time you act, this fortune is already forgotten."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
