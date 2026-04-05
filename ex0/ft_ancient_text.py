import sys
from typing import IO


def recover_text() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f: IO[str] | None = None
    try:
        f = open(filename, 'w')
        content: str = f.read()
        print(
            "---\n\n"
            f"{content.strip()}"
            "\n\n---"
        )

    except PermissionError:
        print(
            "Error: Access denied. You do not have the required "
            f"permissions to read {filename}."
        )
    except IsADirectoryError:
        print(
            f"Error: '{filename}' is a directory, not a file. "
            "Please provide a file path."
        )
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if f:
            f.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    try:
        recover_text()
    except BaseException as e:
        print(e)
