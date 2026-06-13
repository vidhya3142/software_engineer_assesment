import requests
import json
from pathlib import Path

BASE_URL = "https://ca-seassessment-api-dev.happywater-190f264d.northcentralus.azurecontainerapps.io"
API_KEY = "sa_2d29e79fd565cf563bd307d3fe33781f778f2863d177e51416d1ad4ea005238e"

headers = {"Authorization": f"Bearer {API_KEY}"}

def save_full_dataset():
    all_records = []
    page = 1
    Path("data").mkdir(exist_ok=True)

    print("Re-fetching dataset...")
    while True:
        resp = requests.get(f"{BASE_URL}/api/v1/dataset?page={page}", headers=headers)
        data = resp.json()
        records = data.get("data", [])
        all_records.extend(records)
        print(f"Page {page} | Total: {len(all_records)}")
        if not data.get("has_more", False):
            break
        page += 1

    # Save as list of base64 strings
    with open("data/records.json", "w", encoding="utf-8") as f:
        json.dump(all_records, f, separators=(',', ':'))

    print(f"\n Saved {len(all_records)} records to data/records.json")
    
save_full_dataset()