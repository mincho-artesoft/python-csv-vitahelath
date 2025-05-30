import pandas as pd
import re

# 1) Зареждаме CSV файла
df = pd.read_csv("foods_full_merged.csv", low_memory=False)

# 2) Колоните, които ни интересуват
columns = [
    "Food Group",
    "Macronutrient Focus",
    "Processing Level",
    "Culinary Usage",
    "Health Impact",
    "diets",
    "allergens",
]

# 3) Дефинираме как да разделяме клетките по колони
split_patterns = {
    # запетая
    "allergens": r"\s*,\s*",
    "diets":     r"\s*,\s*",
    # запетая ИЛИ ;
    "Culinary Usage":     r"\s*[;,]\s*",
    "Macronutrient Focus": r"\s*[;,]\s*",
    "Food Group":          r"\s*[;,]\s*",
}

# 4) Събираме уникалните стойности
unique_vals = {col: set() for col in columns}

for _, row in df[columns].iterrows():
    for col in columns:
        val = row[col]
        if pd.isna(val):
            continue

        txt = str(val)
        if col in split_patterns:                # трябва ли да се дели?
            parts = re.split(split_patterns[col], txt)
            unique_vals[col].update(p for p in parts if p)
        else:
            unique_vals[col].add(txt)

# 5) Отпечатваме резултата
for col in columns:
    for v in sorted(unique_vals[col]):
        print(f"{col} -> {v}")
