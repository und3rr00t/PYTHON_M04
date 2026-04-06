import sys
from typing import IO


def manage_streams() -> None:
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
        print("---\n")
        sys.stdout.write(content)
        print("\n\n---")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    finally:
        if f_in:
            f_in.close()
            print(f"File '{filename}' closed.")

    print("Transform data:")
    lines: list[str] = content.splitlines()
    transformed: str = ""
    for line in lines:
        transformed += line + "#\n"
    print("---\n")
    sys.stdout.write(transformed)
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file: str = sys.stdin.readline().strip()
    
    if new_file:
        print(f"Saving data to '{new_file}'")
        f_out: IO[str] | None = None
        try:
            f_out = open(new_file, 'w')
            f_out.write(transformed)
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{new_file}': {e}\n "
                "Data not saved.\n"
            )
        finally:
            if f_out:
                f_out.close()
    else:
        print("\nNot saving data.")


if __name__ == "__main__":
    manage_streams()
