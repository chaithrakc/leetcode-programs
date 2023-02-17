from typing import List

import pytest

from easy.p268MissingNumber import SolutionMissingNumber

missing_number_tests = [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8)
]

class TestSolutionMissingNumber:
    sol = SolutionMissingNumber()

    @pytest.mark.parametrize('nums, missing_num',missing_number_tests)
    def test_missing_number(self, nums:List[int], missing_num:int):
        assert self.sol.missingNumber(nums) == missing_num
