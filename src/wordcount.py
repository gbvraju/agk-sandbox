"""wordcount: read UTF-8 text on stdin and print the number of words."""

from __future__ import annotations

import sys


def main() -> int:
    data = sys.stdin.buffer.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        message = "error: input is not valid UTF-8; the input encoding setting must be UTF-8"
        print(message, file=sys.stderr)
        return 2
    print(len(text.split()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
