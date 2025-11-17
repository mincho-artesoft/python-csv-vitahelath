import json
import zlib
import base64
import sys
import random
import re

# --- Configuration ---
VOCABULARY_FILENAME = "vocabulary.json"
BUCKETS_FILENAME = "product_buckets.json"
ORIGINAL_FILENAME = "barcodes.json"
NUMBER_OF_TESTS = 20

def find_product_name(gtin_to_find, sorted_bucket_keys, buckets, id_to_word, decompressed_bucket_cache):
    """
    Finds a GTIN and reconstructs its name by concatenating all stored tokens.
    """
    gtin_as_int = int(gtin_to_find)
    bucket_key_to_use = None
    for key in sorted_bucket_keys:
        if int(key) <= gtin_as_int:
            bucket_key_to_use = key
        else:
            break

    if bucket_key_to_use is None:
        return f"Error: No valid bucket found for GTIN {gtin_to_find}"

    if bucket_key_to_use in decompressed_bucket_cache:
        bucket_content = decompressed_bucket_cache[bucket_key_to_use]
    else:
        base64_encoded_data = buckets[bucket_key_to_use]
        compressed_data = base64.b64decode(base64_encoded_data)
        decompressed_json_bytes = zlib.decompress(compressed_data)
        bucket_content = json.loads(decompressed_json_bytes.decode('utf-8'))
        decompressed_bucket_cache[bucket_key_to_use] = bucket_content

    token_ids = bucket_content.get(gtin_to_find)
    if token_ids is None:
        return f"Error: GTIN {gtin_to_find} not found in its supposed bucket (key: {bucket_key_to_use})."

    # --- SIMPLIFIED RECONSTRUCTION ---
    tokens = [id_to_word.get(str(token_id), "") for token_id in token_ids]
    return "".join(tokens)

def main():
    """
    Main function to load processed data, reconstruct it, and verify against the original.
    """
    print("--- Starting 100% Precision Verification Process ---")

    print("Step 1: Loading data files...")
    try:
        with open(ORIGINAL_FILENAME, 'r', encoding='utf-8') as f:
            original_products = json.load(f)
            original_products_map = {p['code']: p['name'] for p in original_products if 'code' in p and p.get('name') is not None}

        with open(VOCABULARY_FILENAME, 'r', encoding='utf-8') as f:
            id_to_word = json.load(f)

        with open(BUCKETS_FILENAME, 'r', encoding='utf-8') as f:
            buckets = json.load(f)

    except FileNotFoundError as e:
        print(f"ERROR: Could not find a required file: {e.filename}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Could not decode JSON from a file. It might be corrupted. Details: {e}")
        sys.exit(1)

    print("All files loaded successfully.")

    sorted_bucket_keys = sorted(buckets.keys(), key=int)
    decompressed_bucket_cache = {}

    print(f"\nStep 2: Performing {NUMBER_OF_TESTS} random verification checks...")

    if not original_products_map:
        print("ERROR: Original product map is empty. Cannot perform tests.")
        sys.exit(1)

    test_codes = random.sample(list(original_products_map.keys()), k=min(NUMBER_OF_TESTS, len(original_products_map)))
    success_count = 0

    for code in test_codes:
        original_name = original_products_map[code]
        reconstructed_name = find_product_name(code, sorted_bucket_keys, buckets, id_to_word, decompressed_bucket_cache)

        print(f"\nTesting GTIN: {code}")
        print(f"  - Original:      '{original_name}'")
        print(f"  - Reconstructed: '{reconstructed_name}'")

        if reconstructed_name == original_name:
            print("  - Result:        ✅ SUCCESS")
            success_count += 1
        else:
            print("  - Result:        ❌ FAILED")

    print("\n--- Verification Summary ---")
    print(f"{success_count} out of {len(test_codes)} tests passed.")
    if success_count == len(test_codes):
        print("✅ The data pipeline is working correctly with 100% precision!")
    else:
        print("❌ Errors were found. Please review the failed tests above.")

if __name__ == "__main__":
    main()
