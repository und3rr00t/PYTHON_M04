from typing import Tuple


def secure_archive(
        filename: str, action: str = 'read', content: str = ''
        ) -> Tuple[bool, str]:
    """Provides safe access to files using context managers."""
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


if __name__ == "__main__":
    print("== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'read'))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', 'read'))

    print("Using 'secure_archive' to read from a regular file:")
    success, res = secure_archive('ancient_fragment.txt', 'read')
    if success:
        print(f"(True, '{res}')")
    else:
        print(f"({success}, '{res}')")

    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive('vault_copy.txt', 'write', res))
