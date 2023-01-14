from typing import List


class SolutionContainsDuplicate:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for the_num in nums:
            if the_num in hashset:
                return True
            hashset.add(the_num)
        return False

    # Time Complexity: O(n) - for loop
    # Space Complexity: O(n) - set
