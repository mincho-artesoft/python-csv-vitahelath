import pandas as pd

# Зареждаме файловете
foods_df = pd.read_csv("foods111_updated.csv")
categories_df = pd.read_csv("food_category.csv")

# Обединяване по food_category_id = id
merged = pd.merge(
    foods_df,
    categories_df,
    left_on="food_category_id",
    right_on="id",
    how="left"  # left за да запазим всички редове от foods_df
)

# Премахваме дублиращата се колона 'id', ако не ни трябва
merged = merged.drop(columns=["id"])

# Запис в нов CSV
merged.to_csv("foods111_with_categories.csv", index=False)

print("✅ Обединяването е готово. Записано е в foods111_with_categories.csv")
