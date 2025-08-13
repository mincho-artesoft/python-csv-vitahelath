#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

# Пътища
INPUT_CSV = Path("foods_full_merged.csv")
OUTPUT_CSV = Path("foods_full_merged_no_extra.csv")

# Зареждаме CSV
df = pd.read_csv(INPUT_CSV, low_memory=False)

# Колони за премахване
cols_to_remove = [
    "Culinary Usage",
    "Food Group",
    "Health Impact",
    "Macronutrient Focus",
    "Processing Level"
]

# Премахваме ги, ако съществуват
df = df.drop(columns=[c for c in cols_to_remove if c in df.columns])

# Записваме обратно
df.to_csv(OUTPUT_CSV, index=False)

print(f"✅ Новият CSV е записан в: {OUTPUT_CSV}")
