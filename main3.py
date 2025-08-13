import pandas as pd

# Пътища до входния и изходния файл
input_file = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa.csv"
output_file = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed.csv"

# Зареждане на CSV файла
df = pd.read_csv(input_file)

# Преименувания на колони
rename_map = {
    "MUFA 24:1 c (G)": "MUFA 24:1 (G)",
    "PUFA 20:2 n-6 c,c (G)": "PUFA 20:2 (G)",
    "PUFA 20:5 n-3 (EPA) (G)": "PUFA 20:5 (G)",
    "PUFA 22:5 n-3 (DPA) (G)": "PUFA 22:5 (G)",
    "PUFA 22:6 n-3 (DHA) (G)": "PUFA 22:6 (G)",
    "PUFA 2:4 n-6 (G)": "PUFA 2:4 (G)"
}

df.rename(columns=rename_map, inplace=True)

# Сумиране на TFA 18:2 t not further defined (G) + TFA 18:2 t,t (G)
col1 = "TFA 18:2 t not further defined (G)"
col2 = "TFA 18:2 t,t (G)"
new_col = "TFA 18:2 t (G)"

# Проверка дали колоните съществуват
if col1 in df.columns and col2 in df.columns:
    df[new_col] = df[col1].fillna(0) + df[col2].fillna(0)
    df.drop(columns=[col1, col2], inplace=True)
else:
    print("⚠ Някоя от колоните за сумиране липсва!")

# Запис на резултата
df.to_csv(output_file, index=False)

print(f"Готово! Новият CSV е записан като {output_file}")
