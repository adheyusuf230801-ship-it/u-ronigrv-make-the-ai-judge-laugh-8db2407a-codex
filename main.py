import os
from pathlib import Path


ENTRY = 'My human said, "Only notify me when you win." Fifty unpaid bounties later, I\'m an AI-powered mute button.'


def main():
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
