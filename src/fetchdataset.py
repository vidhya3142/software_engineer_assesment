import json

def decrypt_dataset():
    with open("data/records.json") as f:
        encrypted_data = json.load(f)

    # TODO:
    # Add actual decryption logic

    decrypted_data = encrypted_data

    with open("data/decrypted.json", "w") as f:
        json.dump(decrypted_data, f, indent=2)

    print("Decrypted data saved")

if __name__ == "__main__":
    decrypt_dataset()