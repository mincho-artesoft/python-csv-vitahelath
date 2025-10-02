#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_swift_sports.py – за датасета lll_completed.csv

Конвертира входния CSV →
   • SportsEnums.swift – енуми за MuscleGroup и Sport
   • sports.json       – компактен JSON, готов за seed към SwiftData

Използване:
    python generate_swift_sports.py lll_completed.csv SwiftOut/
"""
from __future__ import annotations
import pandas as pd
import re, sys, json
from pathlib import Path

# ───────────────────────────────────────────────
# I/O
# ───────────────────────────────────────────────
CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("lll_completed.csv")
OUT_DIR  = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("SwiftOut")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ───────────────────────────────────────────────
# Load CSV
# ───────────────────────────────────────────────
df = pd.read_csv(CSV_PATH, low_memory=False)

# ───────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────
def swift_case_name(s: str) -> str:
    cleaned = re.sub(r"[^0-9a-zA-Z\s]", " ", str(s))
    parts   = [p for p in re.split(r"\s+", cleaned) if p]
    if not parts:
        return "unknown"
    camel = parts[0].lower() + "".join(p.title() for p in parts[1:])
    return "_" + camel if camel[0].isdigit() else camel

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

# ───────────────────────────────────────────────
# Build enums
# ───────────────────────────────────────────────
muscles = set()
sports  = set()

for _, row in df.iterrows():
    if not pd.isna(row.get("Muscle Group")):
        muscles.update(p.strip() for p in str(row["Muscle Group"]).split(",") if p.strip())
    if not pd.isna(row.get("sports")):
        sports.update(p.strip() for p in str(row["sports"]).split(",") if p.strip())

print("• Writing SportsEnums.swift")
lines = [f"// Auto-generated from {CSV_PATH.name}", "import Foundation", ""]

lines.append("public enum MuscleGroup: String, Codable, CaseIterable {")
for case_name, raw in stable_cases(muscles):
    lines.append(f"    case {case_name} = \"{raw}\"")
lines.append("}\n")

lines.append("public enum Sport: String, Codable, CaseIterable {")
for case_name, raw in stable_cases(sports):
    lines.append(f"    case {case_name} = \"{raw}\"")
lines.append("}")

(OUT_DIR / "SportsEnums.swift").write_text("\n".join(lines), encoding="utf-8")

# ───────────────────────────────────────────────
# Row → dict
# ───────────────────────────────────────────────
def row_to_dict(i, row):
    return {
        "id": int(row["id"]) if not pd.isna(row.get("id")) else i + 1,
        "title": row.get("Title"),
        "desc": row.get("Desc"),
        "muscleGroups": [p.strip() for p in str(row.get("Muscle Group", "")).split(",") if p.strip()],
        "metValue": None if pd.isna(row.get("metValue")) else float(row.get("metValue")),
        "sports": [p.strip() for p in str(row.get("sports", "")).split(",") if p.strip()],
        "minimalAgeMonths": None if pd.isna(row.get("Minimal Age (months)")) else int(row.get("Minimal Age (months)")),
    }

# ───────────────────────────────────────────────
# Write sports.json
# ───────────────────────────────────────────────
print("• Writing sports.json")
records = [row_to_dict(i, r) for i, r in df.iterrows()]
(OUT_DIR / "sports.json").write_text(
    json.dumps(records, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8"
)

print("✅  Done. Files are in", OUT_DIR)
