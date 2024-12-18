from blockchain.blockchain import Blockchain
from blockchain.block import Block


def test_blockchain_instance():
    blockchain = Blockchain()
    genesis_block = Block.genesis()

    assert isinstance(blockchain.chain[0], Block)
    assert blockchain.chain[0].hash == genesis_block.hash


def test_add_block():
    blockchain = Blockchain()
    data = 'a piece of test data'

    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data