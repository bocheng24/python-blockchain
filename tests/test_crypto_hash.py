from util.crypto_hash import crypto_hash

def test_crypto_hash():
    assert crypto_hash(1, [2], '3') == crypto_hash([2], '3', 1)
    assert crypto_hash(1, [2], '3') == 'f5f6103e1b785e1acaec695753512ce84e28a75459022e5caf53368c9b40e6d5'