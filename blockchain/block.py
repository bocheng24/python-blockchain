import time
from crypto_hash import *

class Block:

    def __init__(self, timestamp, lasthash, hash, data):
        self.timestamp = timestamp
        self.lasthash = lasthash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block (\n'
            f'\tTimestamp: {self.timestamp}\n'
            f'\tlasthash: {self.lasthash}\n'
            f'\thash: {self.hash}\n'
            f'\tData: {self.data}\n'
            ')'
        )

    @staticmethod
    def mine_block(last_block, data):
        ts = time.time_ns()
        hash = crypto_hash(ts, last_block.hash, data)

        block = Block(ts, last_block.hash, hash, data)

        return block

    @staticmethod
    def genesis():
        ts = 1
        last_hash = 'genesis_last_hash'
        hash = 'genesis_hash'
        data = []

        return Block(ts, last_hash, hash, data)


def main():
    genesis_block = Block.genesis()

    next_block = Block.mine_block(genesis_block, 'hello')

    print(genesis_block)
    print(next_block)

if __name__ == '__main__':
    main()