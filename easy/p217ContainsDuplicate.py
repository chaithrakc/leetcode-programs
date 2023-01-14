from typing import List


class SolutionContainsDuplicate:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
