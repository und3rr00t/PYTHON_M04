def crisis_handler(filename: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{filename}'")
    try:
        with open(filename, "r") as vault:
            content = vault.read()
            print(f"SUCCESS: Archive recovered {content}")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis mitigated, system monitoring active")


def main() -> None:
    print("CYBER ARCHIVES CRISIS RESPONSE SYSTEM ===")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
