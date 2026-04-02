def create_archive() -> None:
    filename: str = "new_discovery.txt"
    vault = None
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    data: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    try:
        vault = open(filename, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in data:
            vault.write(entry + "\n")
            print(entry)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: Security protocols deny write access.")
    except Exception as e:
        print(f"ERROR: Archive creation failed: {e}")
    finally:
        if vault:
            vault.close()


if __name__ == "__main__":
    create_archive()
