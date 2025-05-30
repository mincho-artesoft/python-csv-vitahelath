#!/usr/bin/env python3
"""
generate_swift_food_full.py

Конвертира foods_full_merged.csv →
   • FoodEnums.swift   – енумите за категориалните колони
   • foods.json        – компактeн JSON, готов за seed към SwiftData

Използване:
    python generate_swift_food_full.py foods_full_merged.csv SwiftOut/
"""

from __future__ import annotations
import pandas as pd
import re, sys, json
from pathlib import Path

# ────────────────────────────────────────────────────────────────────────────
# 1️⃣  I/O
# ────────────────────────────────────────────────────────────────────────────
CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("foods_full_merged.csv")
OUT_DIR  = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("SwiftOut")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ────────────────────────────────────────────────────────────────────────────
# 2️⃣  Load CSV
# ────────────────────────────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH, low_memory=False)

CAT_COLS = [
    "Food Group",
    "Macronutrient Focus",
    "Processing Level",
    "Culinary Usage",
    "Health Impact",
    "diets",
    "allergens",
]

# ➜ Food Group и Macronutrient Focus вече също се разделят по “;” или “,”
SPLIT_PAT = {
    "Food Group":          r"\s*[;,]\s*",
    "Macronutrient Focus": r"\s*[;,]\s*",
    "Culinary Usage":      r"\s*[;,]\s*",
    "diets":               r"\s*,\s*",
    "allergens":           r"\s*,\s*",
}

# ────────────────────────────────────────────────────────────────────────────
# 3️⃣  Helpers
# ────────────────────────────────────────────────────────────────────────────
def swift_case_name(s: str) -> str:
    """Преобразува низ в camelCase подходящ за Swift case."""
    cleaned = re.sub(r"[^0-9a-zA-Z\s]", " ", s)
    parts = [p for p in re.split(r"\s+", cleaned) if p]
    if not parts:
        return "unknown"
    camel = parts[0].lower() + "".join(p.title() for p in parts[1:])
    return "_" + camel if camel[0].isdigit() else camel

UNIT_MAP = dict(UG="µg", MG="mg", G="g", KCAL="kcal")

def unit_of(col: str) -> str:
    """Връща мерната единица от името на колоната, конвертирана в четим вид."""
    m = re.findall(r"\(([^()]+)\)", col)
    if not m:
        return ""
    raw = m[-1].upper().strip()
    for k, v in UNIT_MAP.items():
        raw = raw.replace(k, v)
    return raw

def to_float(x):
    return None if pd.isna(x) else float(x)

# ────────────────────────────────────────────────────────────────────────────
# 4️⃣  Build enums
# ────────────────────────────────────────────────────────────────────────────
enum_vals = {c: set() for c in CAT_COLS}
for _, row in df.iterrows():
    for col in CAT_COLS:
        cell = row[col]
        if pd.isna(cell):
            continue
        if col in SPLIT_PAT:
            enum_vals[col].update(
                p.strip() for p in re.split(SPLIT_PAT[col], str(cell)) if p.strip()
            )
        else:
            enum_vals[col].add(str(cell).strip())

ENUM_TYPES = {
    "Food Group":          "FoodGroup",
    "Macronutrient Focus": "MacronutrientFocus",
    "Processing Level":    "ProcessingLevel",
    "Culinary Usage":      "CulinaryUsage",
    "Health Impact":       "HealthImpact",
    "diets":               "Diet",
    "allergens":           "Allergen",
}

print("• Writing FoodEnums.swift")
enum_lines = [f"// Auto-generated from {CSV_PATH.name}", "import Foundation", ""]
for col in CAT_COLS:
    enum_lines.append(f"public enum {ENUM_TYPES[col]}: String, Codable, CaseIterable {{")
    for raw in sorted(enum_vals[col]):
        enum_lines.append(f"    case {swift_case_name(raw)} = \"{raw}\"")
    enum_lines.append("}\n")
(OUT_DIR / "FoodEnums.swift").write_text("\n".join(enum_lines), encoding="utf-8")

# ────────────────────────────────────────────────────────────────────────────
# 5️⃣  Nutrient mapping – пълен речник
# ────────────────────────────────────────────────────────────────────────────
swift_names = {"id": "id", "name": "name", "category": "category"}

groups = {
    "macros": [
        ("Carbohydrate, by difference (G)", "carbohydrates"),
        ("Protein (G)",                     "protein"),
        ("Total lipid (fat) (G)",           "fat"),
        ("Fiber, total dietary (G)",        "fiber"),
        ("Total Sugars (G)",                "totalSugars"),
    ],
    "lipids_main": [
        ("Fatty acids, total saturated (G)",       "totalSaturated"),
        ("Fatty acids, total monounsaturated (G)", "totalMonounsaturated"),
        ("Fatty acids, total polyunsaturated (G)", "totalPolyunsaturated"),
    ],
    "sfa": [
        ("SFA 4:0 (G)",  "sfa4_0"),
        ("SFA 6:0 (G)",  "sfa6_0"),
        ("SFA 8:0 (G)",  "sfa8_0"),
        ("SFA 10:0 (G)", "sfa10_0"),
        ("SFA 12:0 (G)", "sfa12_0"),
        ("SFA 14:0 (G)", "sfa14_0"),
        ("SFA 16:0 (G)", "sfa16_0"),
        ("SFA 18:0 (G)", "sfa18_0"),
    ],
    "mufa": [
        ("MUFA 16:1 (G)", "mufa16_1"),
        ("MUFA 18:1 (G)", "mufa18_1"),
        ("MUFA 20:1 (G)", "mufa20_1"),
        ("MUFA 22:1 (G)", "mufa22_1"),
    ],
    "pufa": [
        ("PUFA 18:2 (G)",           "pufa18_2"),
        ("PUFA 18:3 (G)",           "pufa18_3"),
        ("PUFA 18:4 (G)",           "pufa18_4"),
        ("PUFA 20:4 (G)",           "pufa20_4"),
        ("PUFA 20:5 n-3 (EPA) (G)", "pufa20_5_n3"),
        ("PUFA 22:5 n-3 (DPA) (G)", "pufa22_5_n3"),
        ("PUFA 22:6 n-3 (DHA) (G)", "pufa22_6_n3"),
    ],
    "vitamins": [
        ("Vitamin A, RAE (UG)",                 "vitaminA_RAE"),
        ("Retinol (UG)",                        "retinol"),
        ("Carotene, alpha (UG)",                "caroteneAlpha"),
        ("Carotene, beta (UG)",                 "caroteneBeta"),
        ("Cryptoxanthin, beta (UG)",            "cryptoxanthinBeta"),
        ("Lutein + zeaxanthin (UG)",            "luteinZeaxanthin"),
        ("Lycopene (UG)",                       "lycopene"),
        ("Thiamin (MG)",                        "vitaminB1_Thiamin"),
        ("Riboflavin (MG)",                     "vitaminB2_Riboflavin"),
        ("Niacin (MG)",                         "vitaminB3_Niacin"),
        ("Vitamin B-6 (MG)",                    "vitaminB6"),
        ("Folate, DFE (UG)",                    "folateDFE"),
        ("Folate, food (UG)",                   "folateFood"),
        ("Folate, total (UG)",                  "folateTotal"),
        ("Folic acid (UG)",                     "folicAcid"),
        ("Vitamin B-12 (UG)",                   "vitaminB12"),
        ("Vitamin B-12, added (UG)",            "vitaminB12Added"),
        ("Vitamin C, total ascorbic acid (MG)", "vitaminC"),
        ("Vitamin D (D2 + D3) (UG)",            "vitaminD"),
        ("Vitamin E (alpha-tocopherol) (MG)",   "vitaminE"),
        ("Vitamin E, added (MG)",               "vitaminEAdded"),
        ("Vitamin K (phylloquinone) (UG)",      "vitaminK"),
    ],
    "minerals": [
        ("Calcium, Ca (MG)", "calcium"),
        ("Iron, Fe (MG)",    "iron"),
        ("Magnesium, Mg (MG)", "magnesium"),
        ("Phosphorus, P (MG)", "phosphorus"),
        ("Potassium, K (MG)",  "potassium"),
        ("Sodium, Na (MG)",    "sodium"),
        ("Selenium, Se (UG)",  "selenium"),
        ("Zinc, Zn (MG)",      "zinc"),
        ("Copper, Cu (MG)",    "copper"),
    ],
    "other": [
        ("Alcohol, ethyl (G)",      "alcoholEthyl"),
        ("Caffeine (MG)",           "caffeine"),
        ("Theobromine (MG)",        "theobromine"),
        ("Choline, total (MG)",     "choline"),
        ("Cholesterol (MG)",        "cholesterol"),
        ("Energy (KCAL)",           "energyKcal"),
        ("Water (G)",               "water"),
        ("weight (G)",              "weightG"),
    ],
}

# добавяме всички CSV-колони ⇢ името на property-то
for grp in groups.values():
    for csv_col, swift_prop in grp:
        swift_names[csv_col] = swift_prop

# ────────────────────────────────────────────────────────────────────────────
# 6️⃣  Row → dict (Codable shape)
# ────────────────────────────────────────────────────────────────────────────
def enum_json(col: str, cell):
    """
    • Ако колоната е в SPLIT_PAT → връща списък (list[str]) или None.
    • Иначе → връща низ (str) или None.
    """
    if pd.isna(cell):
        return None
    if col in SPLIT_PAT:
        return [p.strip() for p in re.split(SPLIT_PAT[col], str(cell)) if p.strip()]
    return str(cell).strip()

def nut(row, csv_col):
    """Връща дикт с value+unit, готов за JSON."""
    return {"value": to_float(row[csv_col]), "unit": unit_of(csv_col)}

def row_to_dict(row):
    d = {
        "id": int(row["id"]),
        "name": row["name"],
        "category": row["category"],

        "foodGroup":          enum_json("Food Group", row["Food Group"]),
        "macronutrientFocus": enum_json("Macronutrient Focus", row["Macronutrient Focus"]),
        "processingLevel":    enum_json("Processing Level", row["Processing Level"]),
        "culinaryUsage":      enum_json("Culinary Usage", row["Culinary Usage"]),
        "healthImpact":       enum_json("Health Impact", row["Health Impact"]),
        "diets":              enum_json("diets", row["diets"]),
        "allergens":          enum_json("allergens", row["allergens"]),
    }

    d["macronutrients"] = {
        swift_names[c]: nut(row, c) for c, _ in groups["macros"]
    }
    d["lipids"] = {
        swift_names[c]: nut(row, c)
        for sub in ("lipids_main", "sfa", "mufa", "pufa")
        for c, _ in groups[sub]
    }
    d["vitamins"] = {
        swift_names[c]: nut(row, c) for c, _ in groups["vitamins"]
    }
    d["minerals"] = {
        swift_names[c]: nut(row, c) for c, _ in groups["minerals"]
    }
    d["other"] = {
        swift_names[c]: nut(row, c) for c, _ in groups["other"]
    }
    return d

# ────────────────────────────────────────────────────────────────────────────
# 7️⃣  Write foods.json
# ────────────────────────────────────────────────────────────────────────────
print("• Writing foods.json")
records = [row_to_dict(r) for _, r in df.iterrows()]
with (OUT_DIR / "foods.json").open("w", encoding="utf-8") as fp:
    json.dump(records, fp, ensure_ascii=False, separators=(",", ":"))

print("✅  Done. Files are in", OUT_DIR)
