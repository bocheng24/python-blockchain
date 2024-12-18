import time
from util.crypto_hash import *
from dataclasses import dataclass
from typing import Any

@dataclass
class Block:

    timestamp: int
    lasthash: str
    hash: str
    data: Any
    difficulty: int
    nonce: int

    def __repr__(self):
        return (
            'Block (\n'
            f'\tTimestamp: {self.timestamp}\n'
            f'\tlasthash: {self.lasthash}\n'
            f'\thash: {self.hash}\n'
            f'\tData: {self.data}\n'
            f'\tDifficulty: {self.difficulty}\n'
            f'\nNonce: {str(self.nonce)}\n'
            ')'
        )

    @staticmethod
    def mine_block(last_block, data):
        difficulty = last_block.difficulty
        nonce = 0
        last_block_hash = last_block.hash

        def mine_hash(last_block_hash, difficulty, nonce):

            ts = time.time_ns()
            hash = crypto_hash(ts, last_block_hash, data, difficulty, nonce)

            return {
                'timestamp': ts,
                'lasthash': last_block_hash,
                'data': data,
                'difficulty': difficulty,
                'nonce': nonce,
                'hash': hash
            }

        block_data = mine_hash(last_block_hash, difficulty, nonce)

        while block_data['hash'][0 : difficulty] != '0' * difficulty:
            block_data = mine_hash(last_block_hash, difficulty, block_data['nonce'] + 1)

        else:

            block = Block(**block_data)

        return block

    @staticmethod
    def genesis():

        genesis_data = {
            'timestamp': 1,
            'lasthash': 'genesis_last_hash',
            'hash': 'genesis_hash',
            'data': [],
            'difficulty': 3,
            'nonce': 0

        }

        return Block(**genesis_data)


def main():
    genesis_block = Block.genesis()

    next_block = Block.mine_block(genesis_block, 'hello')

    print(genesis_block)
    print(next_block)

if __name__ == '__main__':
    main()