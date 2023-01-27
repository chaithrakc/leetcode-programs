from typing import List


class SolutionFindMin:
    @staticmethod
    def findMin(nums: List[int]) -> int:

        # if the array has only one element
        if len(nums) == 1:
            return nums[0]

        left_ptr = 0
        right_ptr = len(nums) - 1

        # if array in not rotated, the first element will always be the minimum
        if nums[left_ptr] < nums[right_ptr]:
            return nums[left_ptr]

        while left_ptr < right_ptr:
            mid_ptr = (right_ptr + left_ptr)//2

            if nums[mid_ptr] > nums[mid_ptr+1]:
                return nums[mid_ptr + 1] # found min element on the right hand side

            if nums[mid_ptr - 1] > nums[mid_ptr]:
                return nums[mid_ptr] # found min element on the left hand side

            if nums[mid_ptr] > nums[left_ptr]: # search on right hand side
                left_ptr = mid_ptr + 1

            elif nums[mid_ptr] < nums[left_ptr]: # search on left hand side
                right_ptr = mid_ptr - 1