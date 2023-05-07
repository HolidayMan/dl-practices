import pytest

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


def test_eq():
    assert U64(2**64-1) == U64(2**64-1)
    assert U64(2**64-1) == 2**64-1


def test_floordiv():
    assert U64(2**64-1) // U64(2) == U64(2**63-1)
    assert U64(2**64-1) // 2 == U64(2**63-1)


def test_repr():
    assert repr(U64(2**64-1)) == "U64(18446744073709551615)"


def test_hex_init_error():
    with pytest.raises(ValueError):
        U64.from_hex("1234567890abcdefg")


def test_mod():
    assert U64(2**64-1) % U64(2) == U64(1)
    assert U64(2**64-1) % 2 == U64(1)


def test_lower_than():
    assert U64(0) < U64(2**64-1)
    assert U64(0) < 2**64-1
