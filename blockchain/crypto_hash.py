import hashlib
import json

def crypto_hash(*args):
    stringified_data = sorted([json.dumps(data) for data in args])

    joined_data = ''.join(stringified_data)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    data = [1]

    print(f'crypto_hash("{data}"):', crypto_hash(data))
    print(f'crypto_hash(2, ["ae"], "c"):', crypto_hash(2, ["ae"], "c"))
    print(f'crypto_hash("c", ["ae"], 2):', crypto_hash("c", ["ae"], 2))

if __name__ == '__main__':
    main()