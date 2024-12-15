from block import Block

class Blockchain:

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        new_block = Block(data)

        self.chain.append(new_block)

    def __repr__(self):
        return f'Blockchain - {self.chain}'
    

def main():
    blockchain = Blockchain()

    blockchain.add_block('abc')
    blockchain.add_block('dev')

    print(blockchain)

if __name__ == '__main__':
    main()