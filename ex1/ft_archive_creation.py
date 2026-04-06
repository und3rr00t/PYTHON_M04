import sys
from typing import IO


def create_archive() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f_in: IO[str] | None = None
    content: str = ""
    try:
        f_in = open(filename, 'r')
        content = f_in.read()
        print(
            "---\n\n"
            f"{content.strip()}"
            "\n\n---"
        )
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if f_in:
            f_in.close()
            print(f"File '{filename}' closed.\n")

    print("Transform data:")
    print("---\n")
    lines: list[str] = content.splitlines()
    transformed: str = ""
    for line in lines:
        transformed_line = line + "#\n"
        transformed += transformed_line
        print(transformed_line, end='')
    print("\n---")

    f_out: IO[str] | None = None
    try:
        new_file: str = input("Enter new file name (or empty): ")
        if new_file:
            print(f"Saving data to '{new_file}'")
            f_out = open(new_file, 'w')
            f_out.write(transformed)
            print(f"Data saved in file '{new_file}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"\nError saving file {e}")
    finally:
        if f_out:
            f_out.close()


if __name__ == "__main__":
    create_archive()

