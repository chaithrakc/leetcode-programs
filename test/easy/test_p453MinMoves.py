from typing import List
import pytest

from easy.p453MinMoves import SolutionMinMoves

min_move_tests = [
    ([1, 2, 3], 3),
    ([1, 1, 1], 0),
    ([1, 2, 3, 4, 5], 10)
]


class TestSolutionMinMoves:
    solution = SolutionMinMoves()

    @pytest.mark.parametrize('nums, min_moves', min_move_tests)
    def test_min_moves(self, nums: List[int], min_moves: int) -> None:
        assert self.solution.min_moves(nums) == min_moves
