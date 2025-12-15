import json
import os

def split_workout_plans(input_files, chunk_size=5, output_folder="split_output_files"):
    all_plans = []

    print("--- Започва четенето на файловете ---")
    
    # 1. Четене и обединяване на данните
    for filename in input_files:
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_plans.extend(data)
                        print(f"Успешно зареден: {filename} ({len(data)} плана)")
                    else:
                        print(f"Внимание: {filename} не съдържа списък и ще бъде пропуснат.")
            except Exception as e:
                print(f"Грешка при четене на {filename}: {e}")
        else:
            print(f"Файлът липсва: {filename}")

    total_plans = len(all_plans)
    print(f"\nОбщо намерени планове: {total_plans}")
    
    if total_plans == 0:
        print("Няма данни за обработка.")
        return

    # 2. Създаване на папката, ако не съществува
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
            print(f"Създадена е папка: {output_folder}")
        except OSError as e:
            print(f"Грешка при създаване на папка: {e}")
            return
    else:
        print(f"Папката '{output_folder}' вече съществува. Файловете ще бъдат записани там.")

    # 3. Разбиване на части и записване в папката
    print(f"\n--- Започва разбиване на файлове по {chunk_size} плана ---")
    
    part_num = 1
    for i in range(0, total_plans, chunk_size):
        chunk = all_plans[i : i + chunk_size]
        
        filename = f"final_plans_batch_{part_num:03d}.json"
        # Създаваме пълния път: папка/име_на_файл
        output_path = os.path.join(output_folder, filename)
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(chunk, f, ensure_ascii=False, indent=2)
            print(f"Записан: {output_path} (съдържа {len(chunk)} плана)")
            part_num += 1
        except Exception as e:
            print(f"Грешка при запис на {output_path}: {e}")

    print(f"\nГотово! Всички {part_num-1} файла са в папка '{output_folder}'.")

# Списък с входните файлове
files_list = [
    "plans_part_01_of_05_updated.json",
    "plans_part_02_of_05_updated.json",
    "plans_part_03_of_05_updated.json",
    "plans_part_04_of_05_updated.json",
    "plans_part_05_of_05_updated.json"
]

# Изпълнение
if __name__ == "__main__":
    # chunk_size=5 означава по 5 плана във файл
    # output_folder е името на папката, където ще се запишат
    split_workout_plans(files_list, chunk_size=5, output_folder="split_output_files")