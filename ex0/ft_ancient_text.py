def recover_ancient_text() -> None:
    """Accesses Storage Vault 7 to recover ancient fragments[cite: 136]."""
    filename: str = "ancient_fragment.txt"
    vault = None
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        fragment: str = vault.read()
        print(fragment)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(
           "ERROR: Storage vault not found. Run data generator first."
        )
    except PermissionError:
        print(
            "ACCESS DENIED: Insufficient permissions "
            "to access the storage vault.\n"
            "Please check your access rights and try again."
        )
    except IsADirectoryError:
        print(
            "ERROR: The specified path is a directory, not a data fragment.\n"
            "STATUS: Access protocol aborted to prevent system instability."
        )
    except Exception as e:
        print(f"ERROR: Unexpected system anomaly: {e}")
    finally:
        if vault:
            vault.close()


if __name__ == "__main__":
    recover_ancient_text()
