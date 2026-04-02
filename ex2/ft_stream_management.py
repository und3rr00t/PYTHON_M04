import sys


def manage_streams() -> None:
    print("CYBER ARCHIVES")
    print("COMMUNICATION SYSTEM\n")

    try:

        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        archivist_id: str = sys.stdin.readline().strip()

        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush()
        status: str = sys.stdin.readline().strip()

        sys.stdout.write(
            f"\nge[STANDARD] Archive status from {archivist_id}: {status}\n"
        )

        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n"
        )

        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.write("\nThree-channel communication test successful.\n")
    except EOFError:
        print("\nERROR: Input stream interrupted.")
    except Exception as e:
        sys.stderr.write(f"[ALERT] Unexpected communication error: {e}\n")


if __name__ == "__main__":
    manage_streams()
