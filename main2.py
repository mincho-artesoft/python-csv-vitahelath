import csv

INPUT_FILE = "foods_merged.csv"
OUTPUT_FILE = "foods_names_with_id.csv"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as infile, \
         open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)

        # Заглавен ред
        writer.writerow(["id", "name"])

        # За всеки ред от оригиналния CSV
        for idx, row in enumerate(reader, start=1):
            name = (row.get("name") or "").strip()
            writer.writerow([idx, name])

    print(f"Готово! Създаден е файл: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
