#!/bin/bash

# ==============================================================================
# Xcode Imageset Generator
#
# Създава .imageset папка от SVG файл, готова за използване в Xcode.
#
# Употреба:
#   ./create_imageset.sh <път/до/вашия-файл.svg>
#
# Пример:
#   ./create_imageset.sh agility-icon.svg
#
# Зависимости:
#   - librsvg (инсталира се с 'brew install librsvg')
# ==============================================================================

# Проверка дали е подаден файл като аргумент
if [ "$#" -ne 1 ]; then
    echo "Грешка: Моля, посочете път до SVG файла."
    echo "Пример: $0 path/to/icon.svg"
    exit 1
fi

# Проверка дали инструментът rsvg-convert е наличен
if ! command -v rsvg-convert &> /dev/null; then
    echo "Грешка: Командата 'rsvg-convert' не е намерена."
    echo "Моля, инсталирайте я с 'brew install librsvg'"
    exit 1
fi

# Дефиниране на променливи
INPUT_SVG_PATH="$1"
BASENAME=$(basename "$INPUT_SVG_PATH" .svg)
IMAGESET_DIR="${BASENAME}.imageset"
OUTPUT_PDF_NAME="${BASENAME}.pdf"

# Проверка дали входният файл съществува
if [ ! -f "$INPUT_SVG_PATH" ]; then
    echo "Грешка: Файлът '$INPUT_SVG_PATH' не съществува."
    exit 1
fi

# Създаване на .imageset папката (ако вече съществува, ще я изтрие и създаде наново)
echo "Създаване на папка: $IMAGESET_DIR"
rm -rf "$IMAGESET_DIR"
mkdir "$IMAGESET_DIR"

# Конвертиране на SVG в PDF вътре в .imageset папката
echo "Конвертиране на '$INPUT_SVG_PATH' в '$OUTPUT_PDF_NAME'"
rsvg-convert -f pdf -o "$IMAGESET_DIR/$OUTPUT_PDF_NAME" "$INPUT_SVG_PATH"

# Създаване на Contents.json файла
echo "Създаване на Contents.json"
cat <<EOF > "$IMAGESET_DIR/Contents.json"
{
  "images" : [
    {
      "filename" : "$OUTPUT_PDF_NAME",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true
  }
}
EOF

echo "Готово! Папката '$IMAGESET_DIR' е създадена успешно."
echo "Просто я плъзнете във вашия Asset Catalog (.xcassets) в Xcode."