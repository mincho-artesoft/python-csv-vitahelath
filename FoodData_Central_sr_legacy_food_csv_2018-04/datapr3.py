import pandas as pd

# 1) Зареждане на данните
foods = pd.read_csv("foods111_with_categories.csv")
nutrients = pd.read_csv("nutrient_updated.csv")
food_nutr = pd.read_csv("food_nutrient.csv")

# 2) Закачане на name_with_unit
fn_named = food_nutr.merge(
    nutrients[["id", "name_with_unit"]],
    left_on="nutrient_id",
    right_on="id",
    how="left"
)

# 3) Pivot
pivot = pd.pivot_table(
    fn_named,
    index="fdc_id",
    columns="name_with_unit",
    values="amount",
    aggfunc="mean"
).reset_index()

pivot.columns.name = None
pivot = pivot.reindex(columns=["fdc_id"] + sorted([c for c in pivot.columns if c != "fdc_id"]))

# 4) Merge с foods
final_df = foods.merge(pivot, on="fdc_id", how="left")

# 5) Добавяме колона weight (G) със стойност 100 за всички редове
final_df["weight (G)"] = 100

# 6) Запис
final_df.to_csv("foods111_enriched.csv", index=False)

print(f"✅ Готово! Записано е в foods111_enriched.csv с {len(final_df)} реда и нова колона 'weight (G)' = 100.")
