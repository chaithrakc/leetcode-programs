import pytest

from easy.p696CountBinarySubstrings import SolutionCountBinarySubstrings

binary_strings = [
    ("00110011", 6),
    ("10101", 4),
]


class TestSolutionCountBinarySubstrings:
    solution = SolutionCountBinarySubstrings()

    @pytest.mark.parametrize('binary_str,num_substrings',binary_strings)
    def test_count_binary_substrings(self, binary_str: str, num_substrings: int) -> None:
        assert self.solution.count_binary_substrings(binary_str) == num_substrings
