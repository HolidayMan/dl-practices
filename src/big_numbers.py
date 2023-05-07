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

    def get_hex(self):
        return ''.join(['0' * (15 - len(x.get_hex())) + x.get_hex() for x in self.value_chunks[::-1]])

    @classmethod
    def from_hex(cls, hex_str: str):
        return cls(hex_str)

    def _clear_leading_zeros(self):
        while len(self.value_chunks) > 0 and self.value_chunks[0] == U64(0):
            self.value_chunks.pop(0)

    def __eq__(self, other):
        print(self.value_chunks, other.value_chunks)
        return self.value_chunks == other.value_chunks

    def __repr__(self):
        return f"BigNumber({self.get_hex()})"

    def __add__(self, other: 'BigNumber'):
        """Add two BigNumber objects."""
        output = BigNumber("0")
        output.value_chunks = []
        carry = U64(0)
        print(self.value_chunks, other.value_chunks)
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
                    print("overflow", res, self.value_chunks[i], other.value_chunks[i], carry)
                    carry = U64(1)
                output.value_chunks.append(res)
        if carry > 0:
            output.value_chunks.append(carry)
        output._clear_leading_zeros()
        return output
