from typing import List

import pytest

from easy.p53MaximumSubarray import SolutionMaxSubarray

maxsum_tests = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23)
]


class TestSolutionMaxSubarray:
    solution = SolutionMaxSubarray()

    @pytest.mark.parametrize('nums, maxsum', maxsum_tests)
    def test_max_subarray(self, nums: List, maxsum: int):
        assert self.solution.max_subarray(nums) == maxsum
