from blockchain.block import Block

class Blockchain:

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))

    def __repr__(self):
        return f'Blockchain ******** \n{self.chain}'


def main():
    blockchain = Blockchain()

    blockchain.add_block('abc')
    blockchain.add_block('dev')

    print(blockchain)

if __name__ == '__main__':
    main()