import pytest

from src.U64 import U64
from src.big_numbers import BigNumber


@pytest.fixture
def first_big_number() -> BigNumber:
    return BigNumber.from_hex("ecbe177452f780242608d2c3207c44cb800058a8be2af1fd2df95effd31846f96c689f7d1763b39")


@pytest.fixture
def second_big_number() -> BigNumber:
    return BigNumber.from_hex("12f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3")


def test_hex_init():
    number = BigNumber.from_hex("1234567890abcdef")
    assert number.value_chunks == [U64(1311768467294899695)]


def test_get_hex(first_big_number):
    assert first_big_number.get_hex() == "ecbe177452f780242608d2c3207c44cb800058a8be2af1fd2df95effd31846f96c689f7d1763b39"


def test_get_bin(first_big_number):
    assert first_big_number.get_bin() == bin(int(first_big_number.get_hex(), 16))[2:]


def test_from_bin():
    assert BigNumber.from_bin("00000000000001010101010101010101010101010101010101010101010101010101010101010") == \
           BigNumber("aaaaaaaaaaaaaaaa")


def test_equality():
    assert BigNumber("123456789012345678901234567890") == BigNumber("123456789012345678901234567890")


def test_add(first_big_number, second_big_number):
    assert first_big_number + second_big_number == \
           BigNumber("ecbe177452f7802555431e1f8dfad4658b1c85e70d855d79bb976e19fe549457dbe32b192481e2c")
    assert BigNumber("ffffffffffffffff") + BigNumber("ffffffffffffffff") == BigNumber("1fffffffffffffffe")


def test_sub(first_big_number, second_big_number):
    assert first_big_number - second_big_number == \
           BigNumber("ecbe177452f78022f6ce8766b2fdb53174e42b6a6ed08680a05b4fe5a7dbf99afcee13e10a45846")
    with pytest.raises(ValueError):
        BigNumber("123456789012345678901234567890") - BigNumber("123456789012345678901234567891")


def test_lt(first_big_number, second_big_number):
    assert not first_big_number < second_big_number
    assert second_big_number < first_big_number


@pytest.mark.skip(reason="Not implemented yet and I really don't know how to do it")
def test_mod(first_big_number, second_big_number):
    assert first_big_number % second_big_number == \
           BigNumber("c6312038cd7073719c4b3586454928939954b4f339980ad4e630eba67e56c2d")


def test_inverse(first_big_number):
    assert ~first_big_number == \
           BigNumber("1341e88bad087fdbd9f72d3cdf83bb347fffa75741d50e02d206a1002ce7b90693976082e89c4c6")


def test_xor(first_big_number, second_big_number):
    assert first_big_number ^ second_big_number == \
           BigNumber("ecbe177452f780250932999f4d02cb518b1c7596f1709a81a06751e5f8240ba7031214e11a7d9ca")


def test_or(first_big_number, second_big_number):
    assert first_big_number | second_big_number == \
           BigNumber("ecbe177452f780252f3adbdf6d7ecfdb8b1c7dbeff7afbfdadff5ffffb3c4fff6f7a9ffd1f7fbfb")


def test_and(first_big_number, second_big_number):
    assert first_big_number & second_big_number == \
           BigNumber("26084240207c048a000008280e0a617c0d980e1a031844586c688b1c0502231")


def test_shift_right_with_int(first_big_number):
    assert first_big_number >> 10 == \
           BigNumber("3b2f85dd14bde009098234b0c81f1132e000162a2f8abc7f4b7e57bff4c611be5b1a27df45d8e")


def test_shift_left_with_int(first_big_number):
    assert first_big_number << 10 == \
           BigNumber("3b2f85dd14bde009098234b0c81f1132e000162a2f8abc7f4b7e57bff4c611be5b1a27df45d8ece400")
