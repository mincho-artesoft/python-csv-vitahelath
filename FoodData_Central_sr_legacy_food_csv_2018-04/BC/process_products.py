import json
import re
import zlib
import base64
import sys
from collections import Counter

# --- Configuration ---
INPUT_FILENAME = "barcodes.json"
VOCABULARY_FILENAME = "vocabulary.json"
BUCKETS_FILENAME = "product_buckets.json"
BUCKET_SIZE = 500
MIN_WORD_FREQUENCY = 1
UNKNOWN_TOKEN_ID = 0

def tokenize(text):
    if not text:
        return []
    return re.findall(r"[\w']+|\s+|[^\w\s]", text)

def main():
    print(f"Loading product data from '{INPUT_FILENAME}'...")
    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
            products = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Input file not found at '{INPUT_FILENAME}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from '{INPUT_FILENAME}'.")
        sys.exit(1)

    print(f"Found {len(products)} products.")

    print("Step 1: Building vocabulary...")
    word_counts = Counter()
    for product in products:
        name = product.get('name')
        if name:
            word_counts.update(tokenize(name))

    frequent_words = [word for word, count in word_counts.items() if count >= MIN_WORD_FREQUENCY]
    frequent_words.sort()

    word_to_id = {word: i + 1 for i, word in enumerate(frequent_words)}
    id_to_word = {i + 1: word for i, word in enumerate(frequent_words)}
    id_to_word[UNKNOWN_TOKEN_ID] = "UNK"
    print(f"Vocabulary created with {len(frequent_words)} unique tokens.")

    print("Step 2: Converting product names to token ID arrays...")
    tokenized_products = []
    for product in products:
        code = product.get('code')
        name = product.get('name')
        if not code or name is None:
            continue

        tokens = tokenize(name)
        token_ids = [word_to_id.get(token, UNKNOWN_TOKEN_ID) for token in tokens]
        tokenized_products.append({'code': code, 'tokens': token_ids})

    print("Step 3: Sorting all products numerically by GTIN...")
    tokenized_products.sort(key=lambda p: int(p['code']))

    print(f"Step 4: Grouping products into buckets of {BUCKET_SIZE}...")
    final_buckets = {}
    for i in range(0, len(tokenized_products), BUCKET_SIZE):
        chunk = tokenized_products[i:i + BUCKET_SIZE]
        if not chunk:
            continue

        bucket_key = chunk[0]['code']
        bucket_content = {p['code']: p['tokens'] for p in chunk}

        json_string = json.dumps(bucket_content, separators=(',', ':'))
        byte_data = json_string.encode('utf-8')
        compressed_data = zlib.compress(byte_data, level=9)
        base64_encoded_data = base64.b64encode(compressed_data).decode('ascii')

        final_buckets[bucket_key] = base64_encoded_data

    print(f"Created {len(final_buckets)} buckets.")

    print(f"Step 5: Saving output files...")
    with open(VOCABULARY_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(id_to_word, f, ensure_ascii=False, indent=2)
    print(f"Vocabulary saved to '{VOCABULARY_FILENAME}'")

    with open(BUCKETS_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(final_buckets, f, separators=(',', ':'))
    print(f"Product buckets saved to '{BUCKETS_FILENAME}'")

    print("\nProcessing complete!")

if __name__ == "__main__":
    main()
