import pandas as pd
import re                     # ← добавихме модула re

# 1) Зареждаме последния файл
df = pd.read_csv("foods_fixed_clean13.csv", encoding="utf-8")

# 2) Замяна: всичко, което започва с "Recipe Component", → "Recipe Component"
df["Culinary Usage"] = df["Culinary Usage"].str.replace(
    r"^Recipe Component.*",        # от началото на низа до края
    "Recipe Component",
    regex=True,
    flags=re.IGNORECASE,
)

# 3) Записваме резултата
df.to_csv("foods_fixed_clean14.csv", index=False, encoding="utf-8")
print("Готово – запазено като foods_fixed_clean14.csv")
