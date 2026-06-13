import requests
import hashlib
import json
import base64
from pathlib import Path

BASE_URL = "https://ca-seassessment-api-dev.happywater-190f264d.northcentralus.azurecontainerapps.io"
API_KEY = "sa_2d29e79fd565cf563bd307d3fe33781f778f2863d177e51416d1ad4ea005238e"

headers = {"Authorization": f"Bearer {API_KEY}"}

def fetch_and_compute():
    all_records = []
    page = 1

    print("Fetching dataset...")
    while True:
        resp = requests.get(f"{BASE_URL}/api/v1/dataset?page={page}", headers=headers)
        data = resp.json()
        records = data.get("data", [])
        all_records.extend(records)
        print(f"Page {page}: {len(records)} | Total: {len(all_records)}")
        
        if not data.get("has_more", False):
            break
        page += 1

    print(f"\n Fetched {len(all_records)} base64 records")

    # === Try Decoded Bytes Concatenation (Very Common for byte-level) ===
    try:
        decoded_bytes = b''.join(base64.b64decode(item) for item in all_records)
        decoded_hash = hashlib.sha256(decoded_bytes).hexdigest()
        print("\n DECODED BYTES CONCAT HASH (Try this first):")
        print(decoded_hash)
    except Exception as e:
        print("Decode error:", e)

    # Other candidates
    print("\nOther candidates:")
    raw_concat = ''.join(all_records)
    print("1. Raw base64 concat:", hashlib.sha256(raw_concat.encode()).hexdigest())
    
    array_minified = json.dumps(all_records, separators=(',', ':'))
    print("2. Pure array:", hashlib.sha256(array_minified.encode()).hexdigest())

    Path("data").mkdir(exist_ok=True)
    Path("data/decoded_hash.txt").write_text(decoded_hash)
    
    print(f"""{{
  "type": "content_hash",
  "value": "{decoded_hash}",
  "notes": "SHA256 of concatenated decoded bytes"
}}""")

if __name__ == "__main__":
    fetch_and_compute()