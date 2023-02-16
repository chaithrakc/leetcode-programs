import pytest

from easy.p190ReverseBits import SolutionReverseBits

reverse_bits_tests =[
    (0b00000010100101000001111010011100, 964176192 ),
    (0b11111111111111111111111111111101, 3221225471 ),
]

class TestSolutionReverseBits:
    solution = SolutionReverseBits()

    @pytest.mark.parametrize('bits, reversed_num', reverse_bits_tests)
    def test_reverse_bits(self, bits:int, reversed_num:int):
        assert self.solution.reverseBits(bits) == reversed_num
