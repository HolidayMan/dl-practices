from typing import Iterable, Sized, Reversible


def chunks(s: Iterable | Sized | Reversible, n: int):
    """Produce `n`-character chunks from `s`."""
    step = n
    if n < 0:
        step = -n
        s = s[::-1]
    for start in range(0, len(s), step):
        if n < 0:
            yield s[start:start+step][::-1]
        else:
            yield s[start:start+step]


def validate_hex(hex_str: str):
    hex_digits = "0123456789abcdef"
    for char in hex_str.lower():
        if char not in hex_digits:
            raise ValueError("Invalid hex string")
    return True
