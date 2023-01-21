from typing import List

import pytest

from search_algorithms.binary_search import BinarySearch

binary_search_tests = [
    ([10, 20, 30, 50, 60, 80, 110, 130, 140, 170], 110, 6),
    ([10, 20, 30, 40, 60, 110, 120, 130, 170], 175, -1)
]
class TestBinarySearch:
    search_obj = BinarySearch()

    @pytest.mark.parametrize('sorted_arr, key, index',binary_search_tests)
    def test_binary_search(self, sorted_arr:List[int], key:int, index:int):
        assert self.search_obj.binary_search(sorted_arr, key) == index
