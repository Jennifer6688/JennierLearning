# string_sha256_hash.py
import hashlib

def get_sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

if __name__ == "__main__":
    s = input("Enter a string: ")
    hash_value = get_sha256_hash(s)
    print(f"The SHA-256 hash of the string is: {hash_value}")
