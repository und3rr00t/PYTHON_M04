import sys
from typing import IO, List


def create_archive() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f_in: IO = None
    content: str = ""
    try:
        f_in = open(filename, 'r')
        content = f_in.read()
        print(content, end='')
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if f_in:
            f_in.close()
            print(f"File '{filename}' closed.")

    # Transformation logic
    print("Transform data:")
    lines: List[str] = content.splitlines()
    transformed: str = ""
    for line in lines:
        transformed_line = line + "#\n"
        transformed += transformed_line
        print(transformed_line, end='')

    new_file: str = input("Enter new file name (or empty): ")
    if new_file:
        print(f"Saving data to '{new_file}'")
        f_out: IO = None
        try:
            f_out = open(new_file, 'w')
            f_out.write(transformed)
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"Error saving file: {e}")
        finally:
            if f_out:
                f_out.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    create_archive()
