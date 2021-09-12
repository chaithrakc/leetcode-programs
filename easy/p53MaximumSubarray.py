# Reference Video https://www.youtube.com/watch?v=86CQq3pKSUw&t=222s

from typing import List


# Kadane's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
class SolutionMaxSubarray:

    def max_subarray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]  # initializing current and max sum to first element
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum
