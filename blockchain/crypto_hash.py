import hashlib
import json

def crypto_hash(data):
    stringified_data = json.dumps(data)

    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
    data = [1]

    print(f'crypto_hash("{data}"):', crypto_hash(data))

if __name__ == '__main__':
    main()