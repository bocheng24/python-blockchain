from blockchain.block import Block


def test_mine_block():

    last_block = Block.genesis()
    data = 'a piece of test data'

    mined_block = Block.mine_block(last_block, data)

    assert isinstance(mined_block, Block)
    assert mined_block.data == data
    assert mined_block.lasthash == last_block.hash
    assert mined_block.hash[0 : mined_block.difficulty] == '0' * mined_block.difficulty


def test_genesis():
    genesis_block = Block.genesis()

    assert isinstance(genesis_block, Block)
    assert genesis_block.timestamp == 1
    assert genesis_block.lasthash == 'genesis_last_hash'
    assert genesis_block.hash == 'genesis_hash'
    assert genesis_block.data == []