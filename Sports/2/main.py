import json
import csv
import os

def load_csv_titles(csv_filename):
    """Зарежда заглавията от CSV файла в set за бързо търсене."""
    titles = set()
    
    if not os.path.exists(csv_filename):
        print(f"ГРЕШКА: Файлът '{csv_filename}' не е намерен!")
        return titles

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Използваме 'Title', както посочи в описанието
                if 'Title' in row and row['Title']:
                    # Нормализираме: малки букви и махане на спейсове отпред/отзад
                    titles.add(row['Title'].strip().lower())
    except Exception as e:
        print(f"Грешка при четене на CSV: {e}")
        
    return titles

def check_exercises_against_csv():
    csv_filename = "lll_completed_normalized.csv"
    
    # 1. Зареждане на валидните имена от CSV
    print("Зареждане на данни от CSV...")
    csv_titles_normalized = load_csv_titles(csv_filename)
    
    if not csv_titles_normalized:
        print("Няма заредени заглавия или файлът е празен. Спиране.")
        return

    print(f"Заредени са {len(csv_titles_normalized)} уникални упражнения от CSV файла.\n")

    # Генериране на имената на JSON файловете
    json_files = [f"plans_part_0{i}_of_05_updated.json" for i in range(1, 6)]
    
    # Сет за съхранение на липсващите упражнения (за да избегнем дубликати при принтиране)
    missing_exercises = set()
    total_checked = 0

    # 2. Обхождане на JSON файловете
    for json_file in json_files:
        if not os.path.exists(json_file):
            print(f"Липсва файл: {json_file}. Пропускане...")
            continue
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # JSON структура: List -> Plan -> sections -> exercises
                for plan in data:
                    sections = plan.get('sections', [])
                    if not sections: continue
                    
                    for section in sections:
                        exercises = section.get('exercises', [])
                        if not exercises: continue
                        
                        for exercise in exercises:
                            ex_name = exercise.get('name')
                            
                            if ex_name:
                                total_checked += 1
                                # Нормализираме името от JSON за проверка
                                ex_name_norm = ex_name.strip().lower()
                                
                                # Проверка дали съществува в CSV списъка
                                if ex_name_norm not in csv_titles_normalized:
                                    # Добавяме оригиналното име (не нормализираното), за да знаеш как точно е написано в JSON-а
                                    missing_exercises.add(ex_name)
                                    
        except Exception as e:
            print(f"Грешка при обработка на {json_file}: {e}")

    # 3. Принтиране на резултатите
    print("-" * 60)
    print(f"РЕЗУЛТАТ: Проверени са общо {total_checked} упражнения в JSON файловете.")
    
    if missing_exercises:
        print(f"Открити са {len(missing_exercises)} уникални имена, които ЛИПСВАТ в CSV файла:")
        print("-" * 60)
        for missing in sorted(list(missing_exercises)):
            print(f"[ЛИПСВА] {missing}")
    else:
        print("СУПЕР! Всички упражнения от JSON файловете съществуват в CSV файла.")
    print("-" * 60)

if __name__ == "__main__":
    check_exercises_against_csv()