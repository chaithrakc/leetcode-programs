import pytest

from easy.p1356SortByBits import SolutionSortByBits

sort_by_bits_testcases = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
    ([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
]


class TestSolutionSortByBits:
    solution = SolutionSortByBits()

    @pytest.mark.parametrize('input_arr, sorted_arr', sort_by_bits_testcases)
    def test_sort_by_bits(self, input_arr, sorted_arr):
        assert self.solution.sort_by_bits(input_arr) == sorted_arr
