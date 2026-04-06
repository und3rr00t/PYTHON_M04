def secure_archive(
        filename: str, action: str = 'read', content: str = ''
        ) -> tuple[bool, str]:
    try:
        if action == 'read':
            with open(filename, 'r') as f:
                return True, f.read()
        elif action == 'write':
            with open(filename, 'w') as f:
                f.write(content)
                return True, "Content successfully written to file"
        return False, "Invalid action"
    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'read'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('inaccessible_file', 'read'))
    
    print("\nUsing 'secure_archive' to read from a regular file:")
    success, res = secure_archive('ancient_fragment.txt', 'read')
    print(f"Result: ({success}, {res!r})")

    if success:
        print("\nUsing 'secure_archive' to write previous content to a new file:")
        write_status = secure_archive('vault_copy.txt', 'write', res)
        print(write_status)


if __name__ == "__main__":
    main()
