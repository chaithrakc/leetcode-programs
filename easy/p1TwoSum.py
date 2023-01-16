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
        hashmap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i  # key:number, value=index
