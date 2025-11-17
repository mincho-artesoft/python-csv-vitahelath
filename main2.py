import csv
from pathlib import Path

# Имена на файловете (смени ако са в друга папка)
FOODS_FILE = Path("foods_filtered_keep_only_names_from_111.csv")
TEST2_FILE = Path("test 2.csv")

# Ако искаш сравнение без значение главни/малки букви – True
CASE_INSENSITIVE = True


def normalize_name(name: str) -> str:
    """Нормализира име за сравнение."""
    if name is None:
        return ""
    name = name.strip()
    if CASE_INSENSITIVE:
        name = name.casefold()
    return name


def load_foods(path: Path):
    """
    Чете foods_filtered_keep_only_names_from_111.csv.
    Връща списък от записи: { 'name', 'norm', 'foods_id' }
    """
    if not path.exists():
        raise FileNotFoundError(f"Файлът не е намерен: {path}")

    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "name" not in reader.fieldnames:
            raise ValueError(
                f"Колона 'name' не е намерена във файла {path}.\n"
                f"Налични колони: {reader.fieldnames}"
            )

        # Проверяваме дали има и колона 'id' в този файл
        foods_id_field = "id" if "id" in reader.fieldnames else None

        items = []
        for row in reader:
            raw_name = row.get("name", "")
            norm = normalize_name(raw_name)
            if not norm:
                continue

            foods_id = None
            if foods_id_field:
                foods_id = (row.get(foods_id_field) or "").strip() or None

            items.append(
                {
                    "name": (raw_name or "").strip(),
                    "norm": norm,
                    "foods_id": foods_id,
                }
            )

    return items


def load_test2(path: Path):
    """
    Чете test 2.csv.
    Връща:
      - списък с записи { 'name', 'norm', 'test2_id' }
      - dict: norm_name -> [test2_id, ...]
    """
    if not path.exists():
        raise FileNotFoundError(f"Файлът не е намерен: {path}")

    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for col in ("name", "id"):
            if col not in reader.fieldnames:
                raise ValueError(
                    f"Колона '{col}' не е намерена във файла {path}.\n"
                    f"Налични колони: {reader.fieldnames}"
                )

        items = []
        name_to_ids = {}

        for row in reader:
            raw_name = row.get("name", "")
            norm = normalize_name(raw_name)
            if not norm:
                continue

            test2_id = (row.get("id") or "").strip() or None

            item = {
                "name": (raw_name or "").strip(),
                "norm": norm,
                "test2_id": test2_id,
            }
            items.append(item)

            name_to_ids.setdefault(norm, []).append(test2_id)

    return items, name_to_ids


def main():
    print(f"Чета имена от: {FOODS_FILE}")
    foods_items = load_foods(FOODS_FILE)
    print(f"Намерени имена в foods: {len(foods_items)}")

    print(f"\nЧета имена от: {TEST2_FILE}")
    test2_items, test2_name_to_ids = load_test2(TEST2_FILE)
    print(f"Намерени имена в test2: {len(test2_items)}")

    # ----- 1) Кои от FOODS ги няма в TEST2 -----
    missing_in_test2 = []
    for item in foods_items:
        if item["norm"] not in test2_name_to_ids:
            missing_in_test2.append(item)

    print("\n================ РЕЗУЛТАТ 1: FOODS → TEST2 ================")
    if not missing_in_test2:
        print("✅ Всички имена от foods_filtered_keep_only_names_from_111.csv се съдържат в test 2.csv")
    else:
        print(f"⚠ Липсващи имена в test 2.csv: {len(missing_in_test2)}")
        print("Списък (име + id от foods ако има):\n")
        for idx, m in enumerate(missing_in_test2, start=1):
            print(
                f"{idx:4d}. name = '{m['name']}' | "
                f"foods_id = {m['foods_id'] if m['foods_id'] is not None else '-'} | "
                f"test2_id = NOT FOUND"
            )

    # ----- 2) Кои от TEST2 ги няма в FOODS -----
    foods_norms = {item["norm"] for item in foods_items}
    missing_in_foods = []
    for item in test2_items:
        if item["norm"] not in foods_norms:
            missing_in_foods.append(item)

    print("\n================ РЕЗУЛТАТ 2: TEST2 → FOODS ================")
    if not missing_in_foods:
        print("✅ Всички имена от test 2.csv се съдържат в foods_filtered_keep_only_names_from_111.csv")
    else:
        print(f"⚠ Имена в test 2.csv, които ги няма във foods: {len(missing_in_foods)}")
        print("Списък (име + id от test2):\n")
        for idx, m in enumerate(missing_in_foods, start=1):
            print(
                f"{idx:4d}. name = '{m['name']}' | "
                f"test2_id = {m['test2_id'] if m['test2_id'] is not None else '-'} | "
                f"foods_id = NOT FOUND"
            )

    print("\nГотово.")


if __name__ == "__main__":
    main()
