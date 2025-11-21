import csv

# Файлове
FILE_NAMES = "foods_names_with_id2.csv"
FILE_MERGED = "foods_merged_with_description.csv"

def main():
    # 1. Извличаме всички name от foods_merged_with_description.csv в сет
    merged_names = set()

    with open(FILE_MERGED, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            if name:
                merged_names.add(name)

    print(f"Loaded {len(merged_names)} names from merged file.")

    # 2. Проверяваме кои name в foods_names_with_id2.csv липсват
    missing = []

    with open(FILE_NAMES, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            if name and name not in merged_names:
                missing.append((row.get("id"), name))

    print(f"\nMISSING RECORDS ({len(missing)}):")
    for record in missing:
        print(record)

if __name__ == "__main__":
    main()
