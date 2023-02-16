import pytest

from easy.p191HammingWeight import SolutionHammingWeight

bitmanipulation_tests = [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31)
]

class TestSolutionBitManipulation:
    solution = SolutionHammingWeight()

    @pytest.mark.parametrize('binary_str, expected_weight',bitmanipulation_tests)
    def test_hamming_weight(self,binary_str:int, expected_weight:int):
        assert self.solution.hamming_weight(binary_str) == expected_weight

    @pytest.mark.parametrize('binary_str, expected_weight', bitmanipulation_tests)
    def test_hamming_weight_optimized(self, binary_str: int, expected_weight: int):
        assert self.solution.hamming_weight_optimized(binary_str) == expected_weight
