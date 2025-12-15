import json
import plistlib # Използваме вградената библиотека за plist

INPUT_FILE = 'frame_map.json'
OUTPUT_FILE = 'Icons.plist'

def generate_plist():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Грешка при четене на {INPUT_FILE}: {e}")
        return

    # Структурата за Alternate Icons
    alternate_icons = {}
    
    for icon_name in data.keys():
        alternate_icons[icon_name] = {
            "CFBundleIconFiles": [icon_name],
            "UIPrerenderedIcon": False
        }

    # Главната структура на Plist файла
    # Забележка: Тук не слагаме PrimaryIcon, само Alternate, за да не презапишем основната
    plist_content = {
        "CFBundleIcons": {
            "CFBundleAlternateIcons": alternate_icons
        },
        # Ако поддържате iPad, дублирайте структурата тук:
        "CFBundleIcons~ipad": {
            "CFBundleAlternateIcons": alternate_icons
        }
    }

    # Записване във файл
    with open(OUTPUT_FILE, 'wb') as f:
        plistlib.dump(plist_content, f)

    print(f"✅ Успешно създаден '{OUTPUT_FILE}' с {len(data)} икони.")

if __name__ == "__main__":
    generate_plist()