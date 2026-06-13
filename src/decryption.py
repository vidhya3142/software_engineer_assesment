# import requests
# import json
# from pathlib import Path

# BASE_URL = "https://ca-seassessment-api-dev.happywater-190f264d.northcentralus.azurecontainerapps.io"
# API_KEY = "sa_2d29e79fd565cf563bd307d3fe33781f778f2863d177e51416d1ad4ea005238e"

# def probe_decryption():
#     print("Probing for decryption info...")
#     payloads = [
#         {"type": "decrypted_hash", "value": "instructions", "notes": ""},
#         {"type": "decrypted_hash", "value": "key", "notes": ""},
#         {"type": "decrypted_hash", "value": "algorithm", "notes": ""},
#         {"type": "decrypted_hash", "value": "help", "notes": ""},
#     ]
    
#     headers = {"Authorization": f"Bearer {API_KEY}"}
    
#     for p in payloads:
#         resp = requests.post(f"{BASE_URL}/api/v1/submit", headers=headers, json=p)
#         print(f"\nValue: {p['value']}")
#         print(resp.json())

# if __name__ == "__main__":
#     probe_decryption()

import json
import hashlib
from pathlib import Path

# Load the records
with open("data/records.json", "r") as f:
    records = json.load(f)

print(f"Loaded {len(records)} records")

# Save for easy use
Path("data").mkdir(exist_ok=True)
with open("data/records.json", "w") as f:
    json.dump(records, f, separators=(',', ':'))

print("Ready for decryption once we have the key.")