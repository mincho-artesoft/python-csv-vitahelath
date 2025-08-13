import pandas as pd

# Път до CSV файла
file_path = "foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed.csv"

# Четене на CSV
df = pd.read_csv(file_path)

# Принтиране на имената на колоните в азбучен ред
for col in sorted(df.columns):
    print(col)

# Принтиране на броя на колоните
print(f"\nОбщ брой колони: {len(df.columns)}")
