from typing import Union

from src.U64 import U64
from src.utils import chunks, validate_hex


class BigNumber:
    """stores the value_chunks as array of chunks (U64) of up to 16 hex digits each"""
    value_chunks: list[U64] = []

    def __init__(self, hex_str: str):
        hex_str = hex_str.lower()
        validate_hex(hex_str)
        output = []
        for chunk in chunks(hex_str, -16):
            chunk_value = U64.from_hex(chunk)
            output.append(chunk_value)
        self.value_chunks = output
        self._clear_leading_zeros()

    def get_hex(self):
        output = ''.join(['0' * (15 - len(x.get_hex())) + x.get_hex() for x in self.value_chunks[::-1]])
        return output.lstrip('0') or '0'

    def get_bin(self, remove_leading_zeros: bool = True):
        """Get binary representation of a BigNumber object."""
        output = ""
        for chunk in self.value_chunks[::-1]:
            output += '0' * (64 - len(chunk.get_bin())) + chunk.get_bin()
        return output.lstrip('0') or '0' if remove_leading_zeros else output

    @classmethod
    def from_bin(cls, bin_str: str):
        """Create a BigNumber object from binary string."""
        output = BigNumber("0")
        output.value_chunks = []
        for chunk in chunks(bin_str, -64):
            output.value_chunks.append(U64.from_bin(chunk))
        output._clear_leading_zeros()
        return output

    @classmethod
    def from_hex(cls, hex_str: str):
        return cls(hex_str)

    def _clear_leading_zeros(self):
        while len(self.value_chunks) > 0 and self.value_chunks[len(self.value_chunks) - 1] == U64(0):
            self.value_chunks.pop(-1)

    def __eq__(self, other):
        return self.value_chunks == other.value_chunks

    def __repr__(self):
        return f"BigNumber({self.get_hex()})"

    def __add__(self, other: 'BigNumber'):
        """Add two BigNumber objects."""
        output = BigNumber("0")
        output.value_chunks = []
        carry = U64(0)
        for i in range(max(len(self.value_chunks), len(other.value_chunks))):
            if i >= len(self.value_chunks):
                output.value_chunks.append(other.value_chunks[i] + carry)
                carry = U64(0)
            elif i >= len(other.value_chunks):
                output.value_chunks.append(self.value_chunks[i] + carry)
                carry = U64(0)
            else:
                res = self.value_chunks[i] + other.value_chunks[i] + carry
                carry = U64(0)
                if res < self.value_chunks[i] or res < other.value_chunks[i]:
                    carry = U64(1)
                output.value_chunks.append(res)
        if carry > 0:
            output.value_chunks.append(carry)
        output._clear_leading_zeros()
        return output

    def __sub__(self, other: 'BigNumber'):
        """Subtract two BigNumber objects."""
        if self < other:
            raise ValueError("Negative result")
        output = BigNumber("0")
        output.value_chunks = []
        carry = U64(0)
        for i in range(max(len(self.value_chunks), len(other.value_chunks))):
            if i >= len(self.value_chunks):
                output.value_chunks.append(other.value_chunks[i] - carry)
                carry = U64(0)
            elif i >= len(other.value_chunks):
                output.value_chunks.append(self.value_chunks[i] - carry)
                carry = U64(0)
            else:
                res = self.value_chunks[i] - other.value_chunks[i] - carry
                carry = U64(0)
                if res > self.value_chunks[i]:
                    carry = U64(1)
                output.value_chunks.append(res)
        if carry > 0:
            output.value_chunks.append(carry)
        output._clear_leading_zeros()
        return output

    def __lt__(self, other: 'BigNumber'):
        """Compare two BigNumber objects."""
        if len(self.value_chunks) < len(other.value_chunks):
            return True
        if len(self.value_chunks) > len(other.value_chunks):
            return False
        for i in range(len(self.value_chunks) - 1, -1, -1):
            if self.value_chunks[i] < other.value_chunks[i]:
                return True
            if self.value_chunks[i] > other.value_chunks[i]:
                return False
        return False

    def __mod__(self, other: 'BigNumber'):
        """Modulo two BigNumber objects."""
        raise NotImplementedError("Modulo not implemented")

    def __invert__(self):
        """Bitwise invert a BigNumber object."""
        hex_str = self.get_hex()
        output = ""
        for char in hex_str:
            output += (BigNumber('f') - BigNumber(char)).get_hex()
        return BigNumber(output)

    def __process_binary_operation(self, other, operation: callable) -> 'BigNumber':
        hex_str = self.get_hex()
        other_hex_str = other.get_hex()

        if len(hex_str) < len(other_hex_str):
            hex_str = '0' * (len(other_hex_str) - len(hex_str)) + hex_str
        elif len(hex_str) > len(other_hex_str):
            other_hex_str = '0' * (len(hex_str) - len(other_hex_str)) + other_hex_str

        output = ""
        for i in range(len(hex_str)):
            output += hex(operation(int(hex_str[i], 16), int(other_hex_str[i], 16)))[2:]
        return BigNumber(output)

    def __xor__(self, other: 'BigNumber'):
        """Bitwise XOR two BigNumber objects."""
        return self.__process_binary_operation(other, lambda x, y: x ^ y)

    def __or__(self, other: 'BigNumber'):
        """Bitwise OR two BigNumber objects."""
        return self.__process_binary_operation(other, lambda x, y: x | y)

    def __and__(self, other: 'BigNumber'):
        """Bitwise AND two BigNumber objects."""
        return self.__process_binary_operation(other, lambda x, y: x & y)

    def __lshift__(self, other: int):
        """Bitwise left shift a BigNumber object."""
        binary_string = self.get_bin(remove_leading_zeros=False)
        binary_string += '0' * other
        return BigNumber.from_bin(binary_string)

    def __rshift__(self, other: int):
        """Bitwise right shift a BigNumber object."""
        binary_string = self.get_bin(remove_leading_zeros=False)
        binary_string = binary_string[:-other]
        return BigNumber.from_bin(binary_string)
