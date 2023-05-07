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


def test_equality():
    assert BigNumber("123456789012345678901234567890") == BigNumber("123456789012345678901234567890")


def test_add(first_big_number, second_big_number):
    assert first_big_number + second_big_number ==\
           BigNumber("ecbe177452f7802555431e1f8dfad4658b1c85e70d855d79bb976e19fe549457dbe32b192481e2c")
    assert BigNumber("ffffffffffffffff") + BigNumber("ffffffffffffffff") == BigNumber("1fffffffffffffffe")


def test_sub(first_big_number, second_big_number):
    assert first_big_number - second_big_number == BigNumber("-801329108308638347349900483526598627864127460737381586296519424278317537274212838327072698871466")


def test_mod(first_big_number, second_big_number):
    assert first_big_number % second_big_number == BigNumber("123456789012345890239472389490750289374813270471089237489123748907120893478092137407213089471289")


def test_inverse(first_big_number):
    assert ~first_big_number == BigNumber("-123456789012345890239472389490750289374813270471089237489123748907120893478092137407213089471290")


def test_xor(first_big_number, second_big_number):
    assert first_big_number ^ second_big_number == BigNumber("801964998982331744196666599901880566532934167195810522193172105509257232327518910074878909698778")


def test_or(first_big_number, second_big_number):
    assert first_big_number | second_big_number == BigNumber("925103842657830936012755931204989886573344084437685291733969513800908278278958011608188893756411")


def test_and(first_big_number, second_big_number):
    assert first_big_number & second_big_number == BigNumber("123138843675499191816089331303109320040409917241874769540797408291651045951439101533309984057633")


def test_shift_right_with_int(first_big_number):
    assert first_big_number >> 10 == BigNumber("120563270519869033436984755362060829467591084444423083485472411042110247537199352936731532686")


def test_shift_left_with_int(first_big_number):
    assert first_big_number << 10 == BigNumber("126419751948642191605219726838528296319808788962395379188862718880891794921566348704986203618599936")


def test_shift_right_with_big_number(first_big_number):
    assert first_big_number >> BigNumber("10") == BigNumber("120563270519869033436984755362060829467591084444423083485472411042110247537199352936731532686")


def test_shift_left_with_big_number(first_big_number):
    assert first_big_number << BigNumber("10") == BigNumber("126419751948642191605219726838528296319808788962395379188862718880891794921566348704986203618599936")