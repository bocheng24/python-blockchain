from blockchain.block import Block
from time import sleep, time_ns

from configs.config import MINE_RATE, SECONDS


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


def test_quickly_mined_block_difficulty():
    last_block = Block.mine_block(Block.genesis(), 'one')
    next_block = Block.mine_block(last_block, 'two')

    assert next_block.difficulty == last_block.difficulty + 1


def test_slowly_mined_block_difficulty():
    last_block = Block.mine_block(Block.genesis(), 'one')

    sleep(MINE_RATE / SECONDS)

    next_block = Block.mine_block(last_block, 'two')

    assert next_block.difficulty == last_block.difficulty - 1


def test_difficulty_at_1():
    last_block = Block(
        timestamp=time_ns(),
        lasthash='last_hash',
        hash='hash',
        data='diffculty 1 data',
        difficulty=1,
        nonce=0
    )

    sleep(MINE_RATE / SECONDS)

    next_block = Block.mine_block(last_block, 'two')

    assert next_block.difficulty == last_block.difficulty
    assert next_block.difficulty == 1
