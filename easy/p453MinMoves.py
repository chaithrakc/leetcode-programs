from typing import List


class SolutionMinMoves:
    def min_moves(self, nums: List[int]) -> int:
        nums.sort()
        count_moves = 0
        for index in range(len(nums) - 1, -1, -1):
            count_moves += nums[index] - nums[0]
        return count_moves
