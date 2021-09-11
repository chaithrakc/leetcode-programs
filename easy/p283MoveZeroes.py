from typing import List


class SolutionMoveZeroes:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1: bring all the non-zero elements to beginning of the array
        last_nonzero_found_at = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[last_nonzero_found_at] = nums[index]
                last_nonzero_found_at += 1

        # step 2: fill in all the zeroes
        for index in range(last_nonzero_found_at, len(nums)):
            nums[index] = 0



