from typing import List

from medium.p153FindMinimumRotatedSortedArray import SolutionFindMin
import pytest

find_min_tests = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11)
]


class TestSolutionFindMin:
    solution = SolutionFindMin()

    @pytest.mark.parametrize('sorted_arr, min_val', find_min_tests)
    def test_find_min(self, sorted_arr: List[int], min_val: int):
        assert self.solution.findMin(sorted_arr) == min_val
