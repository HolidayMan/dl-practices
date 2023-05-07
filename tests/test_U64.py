from src.U64 import U64


def test_hex_init():
    assert U64.from_hex("1234567890abcdef") == U64(1311768467294899695)


def test_get_hex():
    assert U64(1311768467294899695).get_hex() == "1234567890abcdef"


def test_get_bin():
    assert U64(1311768467294899695).get_bin() == "1001000110100010101100111100010010000101010111100110111101111"


def test_greater_than():
    assert U64(2**64-1) > U64(0)
    assert U64(2**64-1) > 100


def test_add():
    assert U64(2382398) + U64(1) == U64(2382399)
    assert U64(2**64-1) + U64(2) == U64(1)
    assert U64(2**64-1) + U64(2**64-1) == U64(2**64-2)
