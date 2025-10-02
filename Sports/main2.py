import pandas as pd

# Зареждаме CSV файла
df = pd.read_csv("lll_completed.csv")

# Проверяваме за празни клетки по колони
missing_info = df.isnull().sum() + (df.astype(str).applymap(lambda x: x.strip() == "")).sum()

print("Празни клетки по колони:")
print(missing_info)

# Минимална стойност в колоната Minimal Age (months)
if "Minimal Age (months)" in df.columns:
    # Превръщаме в числово, за да сме сигурни
    df["Minimal Age (months)"] = pd.to_numeric(df["Minimal Age (months)"], errors="coerce")
    min_age = df["Minimal Age (months)"].min()
    print(f"\nМинималната стойност в колоната 'Minimal Age (months)': {min_age}")
else:
    print("\nКолоната 'Minimal Age (months)' не е намерена във файла.")
