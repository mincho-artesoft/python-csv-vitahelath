#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_swift_food_full.py  – версия за НОВИЯ датасет

Конвертира входния CSV →
   • FoodEnums.swift – енумите за категориалните колони (category/diets/allergens)
   • foods.json      – компактен JSON, готов за seed към SwiftData

Използване:
    python generate_swift_food_full.py input.csv SwiftOut/
"""
from __future__ import annotations
import pandas as pd
import re, sys, json
from pathlib import Path

# ────────────────────────────────────────────────────────────────────────
# 1) I/O
# ────────────────────────────────────────────────────────────────────────
CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("foods_union_all_cols_no_max_age_combined_no_d2d3_b12_no_mufa_pufa_renamed.csv")
OUT_DIR  = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("SwiftOut")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ────────────────────────────────────────────────────────────────────────
# 2) Load CSV
# ────────────────────────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH, low_memory=False)

# Запазени категор. колони
CAT_COLS = ["category", "diets", "allergens"]

SPLIT_PAT = {
    "category":  r"\s*[;,]\s*",
    "diets":     r"\s*,\s*",
    "allergens": r"\s*,\s*",
}

# ────────────────────────────────────────────────────────────────────────
# 3) Helpers
# ────────────────────────────────────────────────────────────────────────
def swift_case_name(s: str) -> str:
    cleaned = re.sub(r"[^0-9a-zA-Z\s]", " ", str(s))
    parts   = [p for p in re.split(r"\s+", cleaned) if p]
    if not parts:
        return "unknown"
    camel = parts[0].lower() + "".join(p.title() for p in parts[1:])
    return "_" + camel if camel[0].isdigit() else camel

UNIT_MAP = dict(UG="µg", MG="mg", G="g", KCAL="kcal")

def unit_of(col: str) -> str:
    m = re.findall(r"\(([^()]+)\)", col)
    if not m:
        return ""
    raw = m[-1].upper().strip()
    for k, v in UNIT_MAP.items():
        raw = raw.replace(k, v)
    return raw

def to_float(x):
    return None if pd.isna(x) else float(x)

# ────────────────────────────────────────────────────────────────────────
# 4) Build enums (category/diets/allergens)
# ────────────────────────────────────────────────────────────────────────
enum_vals = {c: set() for c in CAT_COLS}
for _, row in df.iterrows():
    for col in CAT_COLS:
        if col not in df.columns: 
            continue
        cell = row.get(col)
        if pd.isna(cell):
            continue
        if col in SPLIT_PAT:
            enum_vals[col].update(
                p.strip() for p in re.split(SPLIT_PAT[col], str(cell)) if p.strip()
            )
        else:
            enum_vals[col].add(str(cell).strip())

# избягване на колизии при case идентификатори
def stable_cases(values: set[str]) -> list[tuple[str, str]]:
    used = {}
    out = []
    for raw in sorted(values):
        base = swift_case_name(raw)
        name = base
        i = 2
        while name in used:
            name = f"{base}_{i}"
            i += 1
        used[name] = raw
        out.append((name, raw))
    return out

ENUM_TYPES = {"category": "FoodCategory", "diets": "Diet", "allergens": "Allergen"}

print("• Writing FoodEnums.swift")
enum_lines = [f"// Auto-generated from {CSV_PATH.name}", "import Foundation", ""]
for col in CAT_COLS:
    if col not in df.columns: 
        continue
    enum_lines.append(f"public enum {ENUM_TYPES[col]}: String, Codable, CaseIterable {{")
    for case_name, raw in stable_cases(enum_vals[col]):
        enum_lines.append(f"    case {case_name} = \"{raw}\"")
    enum_lines.append("}\n")
(OUT_DIR / "FoodEnums.swift").write_text("\n".join(enum_lines), encoding="utf-8")

# ────────────────────────────────────────────────────────────────────────
# 5) Nutrient mapping – НОВ/РАЗШИРЕН
# ────────────────────────────────────────────────────────────────────────
swift_names = {"name": "name"}  # id ще се добави по-долу

groups = {
    "macros": [
        ("Carbohydrate, by difference (G)", "carbohydrates"),
        ("Protein (G)",                     "protein"),
        ("Total lipid (fat) (G)",           "fat"),
        ("Fiber, total dietary (G)",        "fiber"),
        ("Total Sugars (G)",                "totalSugars"),
    ],

    # Разширени липиди
    "lipids_main": [
        ("Fatty acids, total saturated (G)",        "totalSaturated"),
        ("Fatty acids, total monounsaturated (G)",  "totalMonounsaturated"),
        ("Fatty acids, total polyunsaturated (G)",  "totalPolyunsaturated"),
        ("Fatty acids, total trans (G)",            "totalTrans"),
        ("Fatty acids, total trans-monoenoic (G)",  "totalTransMonoenoic"),
        ("Fatty acids, total trans-polyenoic (G)",  "totalTransPolyenoic"),
    ],
    "sfa": [
        ("SFA 4:0 (G)",  "sfa4_0"),
        ("SFA 6:0 (G)",  "sfa6_0"),
        ("SFA 8:0 (G)",  "sfa8_0"),
        ("SFA 10:0 (G)", "sfa10_0"),
        ("SFA 12:0 (G)", "sfa12_0"),
        ("SFA 13:0 (G)", "sfa13_0"),
        ("SFA 14:0 (G)", "sfa14_0"),
        ("SFA 15:0 (G)", "sfa15_0"),
        ("SFA 16:0 (G)", "sfa16_0"),
        ("SFA 17:0 (G)", "sfa17_0"),
        ("SFA 18:0 (G)", "sfa18_0"),
        ("SFA 20:0 (G)", "sfa20_0"),
        ("SFA 22:0 (G)", "sfa22_0"),
        ("SFA 24:0 (G)", "sfa24_0"),
    ],
    "mufa": [
        ("MUFA 14:1 (G)", "mufa14_1"),
        ("MUFA 15:1 (G)", "mufa15_1"),
        ("MUFA 16:1 (G)", "mufa16_1"),
        ("MUFA 17:1 (G)", "mufa17_1"),
        ("MUFA 18:1 (G)", "mufa18_1"),
        ("MUFA 20:1 (G)", "mufa20_1"),
        ("MUFA 22:1 (G)", "mufa22_1"),
        ("MUFA 24:1 (G)", "mufa24_1"),
        ("TFA 16:1 t (G)", "tfa16_1_t"),
        ("TFA 18:1 t (G)", "tfa18_1_t"),
        ("TFA 22:1 t (G)", "tfa22_1_t"),
        ("TFA 18:2 t (G)", "tfa18_2_t"),  # отделна колона в края
    ],
    "pufa": [
        ("PUFA 18:2 (G)", "pufa18_2"),
        ("PUFA 18:3 (G)", "pufa18_3"),
        ("PUFA 18:4 (G)", "pufa18_4"),
        ("PUFA 20:2 (G)", "pufa20_2"),
        ("PUFA 20:3 (G)", "pufa20_3"),
        ("PUFA 20:4 (G)", "pufa20_4"),
        ("PUFA 20:5 (G)", "pufa20_5"),
        ("PUFA 21:5 (G)", "pufa21_5"),
        ("PUFA 22:4 (G)", "pufa22_4"),
        ("PUFA 22:5 (G)", "pufa22_5"),
        ("PUFA 22:6 (G)", "pufa22_6"),
        ("PUFA 2:4 (G)",  "pufa2_4"),  # странна колона – пазим я, ако съществува
    ],

    # Витамини (вкл. Choline)
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
        ("Pantothenic acid (MG)",               "vitaminB5_PantothenicAcid"),
        ("Vitamin B-6 (MG)",                    "vitaminB6"),
        ("Vitamin B-12 (UG)",                   "vitaminB12"),
        ("Folate, DFE (UG)",                    "folateDFE"),
        ("Folate, food (UG)",                   "folateFood"),
        ("Folate, total (UG)",                  "folateTotal"),
        ("Folic acid (UG)",                     "folicAcid"),
        ("Vitamin C, total ascorbic acid (MG)", "vitaminC"),
        ("Vitamin D (D2 + D3) (UG)",            "vitaminD"),
        ("Vitamin E (MG)",                      "vitaminE"),
        ("Vitamin K (UG)",                      "vitaminK"),
        ("Choline, total (MG)",                 "choline"),
    ],

    # Минерали (допълнени)
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
        ("Manganese, Mn (MG)", "manganese"),
        ("Fluoride, F (UG)",   "fluoride"),
    ],

    # Аминокиселини
    "amino_acids": [
        ("Alanine (G)",         "alanine"),
        ("Arginine (G)",        "arginine"),
        ("Aspartic acid (G)",   "asparticAcid"),
        ("Cystine (G)",         "cystine"),
        ("Glutamic acid (G)",   "glutamicAcid"),
        ("Glycine (G)",         "glycine"),
        ("Histidine (G)",       "histidine"),
        ("Isoleucine (G)",      "isoleucine"),
        ("Leucine (G)",         "leucine"),
        ("Lysine (G)",          "lysine"),
        ("Methionine (G)",      "methionine"),
        ("Phenylalanine (G)",   "phenylalanine"),
        ("Proline (G)",         "proline"),
        ("Threonine (G)",       "threonine"),
        ("Tryptophan (G)",      "tryptophan"),
        ("Tyrosine (G)",        "tyrosine"),
        ("Valine (G)",          "valine"),
        ("Serine (G)",          "serine"),
        ("Hydroxyproline (G)",  "hydroxyproline"),
    ],

    # Захари и нишесте (детайл)
    "carb_details": [
        ("Starch (G)",   "starch"),
        ("Sucrose (G)",  "sucrose"),
        ("Glucose (G)",  "glucose"),
        ("Fructose (G)", "fructose"),
        ("Lactose (G)",  "lactose"),
        ("Maltose (G)",  "maltose"),
        ("Galactose (G)","galactose"),
    ],

    # Стероли
    "sterols": [
        ("Phytosterols (MG)",   "phytosterols"),
        ("Beta-sitosterol (MG)","betaSitosterol"),
        ("Campesterol (MG)",    "campesterol"),
        ("Stigmasterol (MG)",   "stigmasterol"),
    ],

    # Други
    "other": [
         ("Alcohol, ethyl (G)",  "alcoholEthyl"),
         ("Caffeine (MG)",       "caffeine"),
         ("Theobromine (MG)",    "theobromine"),
         ("Cholesterol (MG)",    "cholesterol"),
         ("Energy (KCAL)",       "energyKcal"),
         ("Water (G)",           "water"),
         ("weight (G)",          "weightG"),
         ("Ash (G)",             "ash"),
         ("Betaine (MG)",        "betaine"),
    ],
}

# регистрираме csv_col → swift_prop
for grp in groups.values():
    for csv_col, swift_prop in grp:
        swift_names[csv_col] = swift_prop

# ────────────────────────────────────────────────────────────────────────
# 6) Row → dict
# ────────────────────────────────────────────────────────────────────────
def enum_json(col: str, cell):
    if col not in df.columns: 
        return None
    if pd.isna(cell): 
        return None
    if col in SPLIT_PAT:
        return [p.strip() for p in re.split(SPLIT_PAT[col], str(cell)) if p.strip()]
    return str(cell).strip()

def nut(row, csv_col):
    if csv_col not in df.columns:
        return None
    return {"value": to_float(row.get(csv_col)), "unit": unit_of(csv_col)}

id_col = "id" if "id" in df.columns else None

def row_to_dict(i, row):
    d = {
        "id": int(row[id_col]) if id_col else int(i + 1),
        "name": row["name"],
        "minAgeMonths": (None if "min_age_months" not in df.columns else (
            None if pd.isna(row.get("min_age_months")) else int(row.get("min_age_months"))
        )),
        "category": enum_json("category", row.get("category")),
        "diets":     enum_json("diets", row.get("diets")),
        "allergens": enum_json("allergens", row.get("allergens")),
    }

    # Нутриентни групи (всяка е речник {prop: {value, unit}})
    def pack(keys):
        return {swift_names[c]: nut(row, c) for c in keys if nut(row, c) is not None}

    d["macronutrients"] = pack([c for c, _ in groups["macros"]])
    d["lipids"]         = pack([c for c, _ in (groups["lipids_main"] + groups["sfa"] + groups["mufa"] + groups["pufa"])])
    d["vitamins"]       = pack([c for c, _ in groups["vitamins"]])
    d["minerals"]       = pack([c for c, _ in groups["minerals"]])
    d["aminoAcids"]     = pack([c for c, _ in groups["amino_acids"]])
    d["carbDetails"]    = pack([c for c, _ in groups["carb_details"]])
    d["sterols"]        = pack([c for c, _ in groups["sterols"]])
    d["other"]          = pack([c for c, _ in groups["other"]])

    return d

# ────────────────────────────────────────────────────────────────────────
# 7) Write foods.json
# ────────────────────────────────────────────────────────────────────────
print("• Writing foods.json")
records = [row_to_dict(i, r) for i, r in df.iterrows()]
(OUT_DIR / "foods.json").write_text(
    json.dumps(records, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8"
)

print("✅  Done. Files are in", OUT_DIR)
