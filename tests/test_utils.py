import pytest
from src.utils import chunks, validate_hex


def test_chunks():
    assert list(chunks("1234567890", 2)) == ["12", "34", "56", "78", "90"]
    assert list(chunks("1234567890", 3)) == ["123", "456", "789", "0"]
    assert list(chunks("1234567890", -4)) == ["7890", "3456", "12"]


def test_validate_hex():
    assert validate_hex("0123456789abcdef")
    assert validate_hex("0123456789ABCDEF")
    assert validate_hex("0123456789AbCdEf")
    with pytest.raises(ValueError):
        validate_hex("0123456789AbCdEg")
