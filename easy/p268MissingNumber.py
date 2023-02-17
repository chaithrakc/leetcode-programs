from typing import List


class SolutionMissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # last value in the range 0 - n (inclusive)

        # rest of the values from 0 to (n-1) is subtracted in the for loop
        for i in range(len(nums)):
            res = res + (i - nums[i])
        return res

'''
Algorithm:
nums = [y1, z1, x1]

w0 + x0 + y0 + z0 - (y1 + z1 + x1) = missing number
w0 + (x0 - y1) + (y0 - z1) + (z0 - x1) = missing number
res + (i - nums[i])
w0 = missing number

'''