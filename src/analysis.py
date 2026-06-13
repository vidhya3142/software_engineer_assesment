import json

def analyze():
    with open("data/decrypted.json") as f:
        records = json.load(f)

    total_records = len(records)

    findings = [
        f"Total records: {total_records}"
    ]

    with open("data/findings.txt", "w") as f:
        f.write("\n".join(findings))

    print("Analysis complete")

if __name__ == "__main__":
    analyze()