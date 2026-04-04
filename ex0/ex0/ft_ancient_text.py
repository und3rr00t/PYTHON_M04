import sys
from typing import IO


def recover_text() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f: IO = None
    try:
        f = open(filename, 'r')
        content: str = f.read()
        print(content, end='')
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if f:
            f.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    recover_text()
