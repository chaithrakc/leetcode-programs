from typing import List

import pytest

from medium.p56MergeIntervals import SolutionMergeIntervals

interval_tests = [
    ([[1, 3], [8, 10], [15, 18], [2, 6]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])
]


class TestSolutionMergeIntervals:
    solution = SolutionMergeIntervals()

    @pytest.mark.parametrize('intervals, non_overlapping', interval_tests)
    def test_merge(self, intervals: List[List[int]], non_overlapping: List[List[int]]):
        assert self.solution.merge(intervals) == non_overlapping
