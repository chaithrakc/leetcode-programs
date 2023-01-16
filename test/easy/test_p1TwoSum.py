from typing import List

import pytest

from easy.p1TwoSum import SolutionTwoSum

two_sum_testcases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
]


class TestSolutionTwoSum:
    solution = SolutionTwoSum()

    @pytest.mark.parametrize('nums, target, indices', two_sum_testcases)
    def test_two_sum(self, nums: List[int], target: int, indices: List[int]):
        assert self.solution.two_sum(nums, target) == indices
