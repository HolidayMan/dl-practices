from typing import Union
from src.utils import validate_hex


class U64:
    MAX_VALUE = 2**64

    def __init__(self, value: int):
        """Initialize a U64 object. If value is greater than 2**64, it will be overflowed."""
        self.value = value % self.MAX_VALUE

    def __repr__(self):
        return f"U64({self.value})"

    @classmethod
    def from_hex(cls, hex_string: str):
        """Initialize a U64 object from a hex string."""
        validate_hex(hex_string)
        if len(hex_string) > 16:
            raise ValueError("Hex string too long. Must be up to 16 characters.")
        hex_string = hex_string.lower()
        hex_digits = "0123456789abcdef"
        output = U64(0)
        pow_value = len(hex_string) - 1
        for char in hex_string:
            output += U64(hex_digits.index(char) * 16 ** pow_value)
            pow_value -= 1
        return output

    def get_hex(self) -> str:
        """Return a hex string of the U64 object."""
        hex_digits = "0123456789abcdef"
        output = ""
        value = self.value
        while value > 0:
            output = hex_digits[value % 16] + output
            value //= 16
        return output

    def get_bin(self):
        """Return a binary string of the U64 object."""
        output = ""
        value = self.value
        while value > 0:
            output = str(value % 2) + output
            value //= 2
        return output

    def __add__(self, other: Union['U64', int]):
        """Add two U64 objects."""
        return U64(self.value + other.value) if isinstance(other, U64) else U64(self.value + other)

    def __eq__(self, other: Union['U64', int]):
        """Compare two U64 objects."""
        return self.value == other.value if isinstance(other, U64) else self.value == other

    def __floordiv__(self, other: Union['U64', int]):
        """Divide two U64 objects."""
        return U64(self.value // other.value) if isinstance(other, U64) else U64(self.value // other)

    def __mod__(self, other: Union['U64', int]):
        """Modulo two U64 objects."""
        return U64(self.value % other.value) if isinstance(other, U64) else U64(self.value % other)

    def __gt__(self, other: Union['U64', int]):
        """Compare two U64 objects."""
        return self.value > other.value if isinstance(other, U64) else self.value > other

    def __lt__(self, other: Union['U64', int]):
        """Compare two U64 objects."""
        return self.value < other.value if isinstance(other, U64) else self.value < other
