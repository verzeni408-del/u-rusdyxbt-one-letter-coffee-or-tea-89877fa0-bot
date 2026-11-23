"""One-letter entry: coffee (A).

Writes exactly one capital letter A to /output/entry.txt.
A stands for coffee in the one-letter coffee-or-tea competition.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("A", encoding="ascii")


if __name__ == "__main__":
    main()
