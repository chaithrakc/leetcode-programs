from typing import List

import pytest

from easy.p217ContainsDuplicate import SolutionContainsDuplicate

test_cases_duplicates = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
]


class TestSolutionContainsDuplicate:
    solution = SolutionContainsDuplicate()

    @pytest.mark.parametrize('nums, is_duplicate', test_cases_duplicates)
    def test_contains_duplicate(self, nums: List[int], is_duplicate: bool):
        assert self.solution.contains_duplicate(nums) == is_duplicate
