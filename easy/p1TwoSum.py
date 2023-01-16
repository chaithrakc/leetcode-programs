from typing import List


# hint - So, if we fix one of the numbers, say x, we have to scan
# the entire array to find the next number y which is value - x
# where value is the input parameter.
# Can we change our array somehow so that this search becomes faster?

class SolutionTwoSum:
    @staticmethod
    def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i, j]

    @staticmethod
    def two_sum_optimized(nums: List[int], target: int) -> List[int]:
        prev_nums = dict() # key:number, value=index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_nums:
                return [prev_nums[diff], i]
            prev_nums[nums[i]] = i

    # Time Complexity: O(n)
    # Space Complexity: O(n)
