import pandas as pd

file1 = "foods_full_merged_with_min_age_filtered.csv"
file2 = "foods111_enriched_renamed_no_ids_clean.csv"

# Зареждаме CSV файловете
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Проверяваме дали имат колона 'name'
if 'name' not in df1.columns or 'name' not in df2.columns:
    raise ValueError("Един от файловете няма колона 'name'.")

# Намираме общите имена
common_names = set(df1['name']).intersection(df2['name'])

print(f"📄 Общ брой еднакви имена: {len(common_names)}")
if common_names:
    print("Примерни общи имена:")
    for name in list(common_names)[:10]:
        print(name)
