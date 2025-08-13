import pandas as pd

# Зареждане на файла
nutrients_df = pd.read_csv("nutrient.csv")

# Създаване на нова колона с комбинирани данни
nutrients_df["name_with_unit"] = nutrients_df["name"] + " (" + nutrients_df["unit_name"] + ")"

# Премахване на старите колони
nutrients_df = nutrients_df.drop(columns=["name", "unit_name"])

# Записване в нов CSV
nutrients_df.to_csv("nutrient_updated.csv", index=False)

print("✅ Готово! Записано е в nutrient_updated.csv с новата колона 'name_with_unit'")
