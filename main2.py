import pandas as pd

# Пътища към файловете
path_names = "111_without_asd_names.csv"
path_full  = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed__zeros_except_min_age_cleared.csv"
path_out   = "foods_filtered_keep_only_names_from_111.csv"

# 1) Четем списъка с позволени имена (id,name)
names_df = pd.read_csv(path_names, encoding="utf-8-sig", dtype=str, usecols=["id","name"])
allowed_names = (
    names_df["name"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
)

# 2) Четем големия файл
full_df = pd.read_csv(path_full, encoding="utf-8-sig")

# 3) Филтър: пазим само редове, чието name е в allowed_names
mask = full_df["name"].astype(str).str.strip().isin(allowed_names)
filtered_df = full_df[mask].copy()

# 4) Запис
filtered_df.to_csv(path_out, index=False, encoding="utf-8-sig")

# (незадължително) кратка статистика в конзолата
print(f"Всички редове: {len(full_df)}")
print(f"Останали редове: {len(filtered_df)}")
print(f"Премахнати редове: {len(full_df) - len(filtered_df)}")
print(f"Изходен файл: {path_out}")
