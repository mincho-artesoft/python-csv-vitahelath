import pandas as pd

# Зареждаме CSV файла
df = pd.read_csv("lll_completed.csv")

# 1. Заместваме Kettlebell Sport → Kettlebell Training
df["sports"] = df["sports"].str.replace(
    "Kettlebell Sport", "Kettlebell Training", regex=False
)

# 2. Заместваме Soccer → Football
df["sports"] = df["sports"].str.replace(
    "Soccer", "Football", regex=False
)

# 3. Премахваме избраните спортове
REMOVE_SPORTS = {
    "Military Training",
    "Mobility",
    "Plyometrics",
    "Rehabilitation",
    "Rotational Sports",
    "Sports Performance",
    "Suspension Training",
}

def clean_sports(entry):
    if pd.isna(entry):
        return entry
    sports = [s.strip() for s in str(entry).split(",")]
    # махаме ненужните
    sports = [s for s in sports if s not in REMOVE_SPORTS]
    # премахваме дублирания в рамките на клетката
    sports = list(dict.fromkeys(sports))
    return ", ".join(sports) if sports else None

df["sports"] = df["sports"].apply(clean_sports)

# Сет за уникални спортове
unique_sports = set()
for entry in df["sports"].dropna():
    for sport in str(entry).split(","):
        unique_sports.add(sport.strip())

unique_sports_sorted = sorted(unique_sports)

# Принтираме
for sport in unique_sports_sorted:
    print(sport)

print(f"\nОбщ брой уникални спорта: {len(unique_sports_sorted)}")

# Записваме в нов CSV
df.to_csv("lll_completed_normalized.csv", index=False)
