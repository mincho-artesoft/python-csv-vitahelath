import pandas as pd

# Зареждаме последния файл
df = pd.read_csv("foods_fixed_clean9.csv", encoding="utf-8")

# Име на колоната, която проверяваме
col = "Food Group"

# Маска за „празно“: NaN ИЛИ празен низ (след .strip() за всеки случай)
empty_mask = df[col].isna() | (df[col].astype(str).str.strip() == "")

# Колко реда са празни?
num_empty = empty_mask.sum()

if num_empty == 0:
    print(f"Няма празни стойности в колоната “{col}”.")
else:
    print(f"Празни стойности в колоната “{col}”: {num_empty} ред(а)")
    # Показваме индексите (0-based) и съответните номера на редовете (1-based)
    indices = empty_mask[empty_mask].index
    print("  Индекси 0-based:", indices.tolist())
    print("  Номера на редовете (1-based):", (indices + 1).tolist())
