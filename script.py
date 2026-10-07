import hashlib
from datetime import datetime
import os

def generate_proof(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return None

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    file_fingerprint = sha256_hash.hexdigest()

    log_entry = f"File: {os.path.basename(file_path)} | Time: {timestamp} | SHA-256: {file_fingerprint}\n"

    with open("proof_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print("--- Proof Generated Successfully ---")
    print(f"Timestamp: {timestamp}")
    print(f"SHA-256 Fingerprint: {file_fingerprint}")
    print("Logged locally to 'proof_log.txt'.")

    return file_fingerprint

if __name__ == "__main__":
    sample_path = input("Enter the path to your screenshot/file: ").strip()
    generate_proof(sample_path)