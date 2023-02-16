from typing import List

import pytest

from easy.p338CountingBits import SolutionCountBits

count_bits_tests = [
    (2, [0,1,1]),
    (5, [0,1,1,2,1,2])
]

class TestSolutionCountBits:
    solution = SolutionCountBits()

    @pytest.mark.parametrize('n, ans',count_bits_tests)
    def test_count_bits(self, n:int, ans:List[int]):
        assert self.solution.count_bits(n) == ans
