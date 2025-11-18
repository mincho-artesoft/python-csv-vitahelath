import pandas as pd
import re
from pathlib import Path

# Настройки
INPUT_CSV = "foods_with_ph.csv"
OUTPUT_DIR = Path("duplicate_names")  # папка за изходните csv файлове


def slugify(value: str) -> str:
    """
    Прави името безопасно за име на файл:
    - маха специални символи
    - заменя ги с долна черта
    - прави всичко lower-case
    """
    value = str(value)
    value = re.sub(r"[^0-9a-zA-Z]+", "_", value)
    value = value.strip("_").lower()
    return value or "unnamed"


def main():
    # 1. Зареждаме CSV файла
    df = pd.read_csv(INPUT_CSV)

    # 2. Намираме имената, които се срещат повече от веднъж
    counts = df["name"].value_counts()
    duplicate_names = counts[counts > 1]

    if duplicate_names.empty:
        print("❗ Няма повтарящи се имена в колоната 'name'.")
        return

    # Създаваме папка за изходните файлове
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("✅ Намерени са дублирани имена:\n")

    # За общ лог, който после ще запишем в CSV
    log_rows = []

    # 3. За всяко име с дубликати:
    for name_value, count in duplicate_names.items():
        # Вземаме всички редове за това име
        group = df[df["name"] == name_value]

        # Реалните номера на редовете във файла:
        # - pandas index е 0-базиран
        # - ред 1 е header
        # -> line_number = index + 2
        line_numbers = group.index + 2

        print(f"Име: {name_value!r} (общо {count})")
        print(
            "  Редове във файла (1-базирано, header е ред 1): "
            + ", ".join(str(n) for n in line_numbers)
        )

        # Добавяме в общия лог
        for idx in group.index:
            log_rows.append(
                {
                    "name": name_value,
                    "row_index_0_based": int(idx),
                    "csv_line_number": int(idx) + 2,  # с включен header
                }
            )

        # 4. Записваме тези редове в отделен CSV файл
        safe_name = slugify(name_value)
        out_file = OUTPUT_DIR / f"dupes_{safe_name}.csv"
        group.to_csv(out_file, index=False)

        print(f"  -> Записано в файл: {out_file}\n")

    # 5. Допълнителен общ лог в CSV
    log_df = pd.DataFrame(log_rows)
    log_csv_path = OUTPUT_DIR / "duplicate_names_log.csv"
    log_df.to_csv(log_csv_path, index=False)

    print(f"📄 Пълен лог за всички дубликати е записан в: {log_csv_path}")


if __name__ == "__main__":
    main()
