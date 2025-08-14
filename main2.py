#!/usr/bin/env python3
import pandas as pd

in_path = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed.csv"
out_path = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed__zeros_except_min_age_cleared.csv"

# Чети всичко като текст, за да не стават NaN/float автом.
df = pd.read_csv(in_path, dtype=str, keep_default_na=False, na_filter=False, low_memory=False)

# Намери точната(ите) колона(и) за пропускане (robust към регистър и интервали в имената)
skip_cols = [c for c in df.columns if c.strip().lower() == "min_age_months"]

# Колони за обработка = всички минус skip
target_cols = [c for c in df.columns if c not in skip_cols]

# Шаблон за "само нули" (вкл. +0, -0, 0.0, 0,00, с интервали)
zero_pattern = r'^\s*[+-]?0+(?:[.,]0+)?\s*$'

# Замяна само в target_cols
df[target_cols] = df[target_cols].replace(to_replace=zero_pattern, value="", regex=True)

# Запис
df.to_csv(out_path, index=False)
print(f"Готово. Записано в: {out_path}")
