import pandas as pd

# 1) Четем CSV файловете
foods = pd.read_csv("foods_merged.csv")          # има колона: name (+ всички нутриенти)
enriched = pd.read_csv("enriched_foods.csv")     # колони: ID, Name, description

# 2) Нормализираме имената (без главни/малки, без празни интервали в края/началото)
foods["name_norm"] = foods["name"].astype(str).str.strip().str.lower()
enriched["name_norm"] = enriched["Name"].astype(str).str.strip().str.lower()

# 3) Оставяме само нужните полета от enriched (Name не ни трябва, ако match-ваме по name_norm)
enriched_small = enriched[["name_norm", "description"]].drop_duplicates(subset=["name_norm"])

# 4) LEFT JOIN от foods към enriched по нормализираното име
merged = foods.merge(enriched_small, on="name_norm", how="left")

# 5) Премахваме помощната колона name_norm
merged = merged.drop(columns=["name_norm"])

# 6) Записваме резултата в нов CSV
merged.to_csv("foods_merged_with_description.csv", index=False)

print("Готово! Записано е в foods_merged_with_description.csv")
