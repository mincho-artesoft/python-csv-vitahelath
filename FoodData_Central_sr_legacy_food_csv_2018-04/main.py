import pandas as pd

# Зареждане на CSV файла
df = pd.read_csv("foods_union_all_cols_no_max_age.csv")

# Функция за извличане на уникални стойности от колона със запетая-разделител
def get_unique_values(column):
    unique_values = set()
    for cell in df[column].dropna():  # махаме NaN
        parts = [x.strip() for x in str(cell).split(",") if x.strip()]  # почистване
        unique_values.update(parts)
    return unique_values

# Уникални за diets
unique_diets = get_unique_values("diets")
print(f"Колона 'diets' → {len(unique_diets)} уникални стойности:")
print(sorted(unique_diets))

# Уникални за allergens
unique_allergens = get_unique_values("allergens")
print(f"\nКолона 'allergens' → {len(unique_allergens)} уникални стойности:")
print(sorted(unique_allergens))
