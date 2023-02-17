from typing import List


class SolutionMissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)  # last value in the range 0 - n (inclusive)

        # rest of the values from 0 to (n-1) is subtracted in the for loop
        for i in range(len(nums)):
            res = res + (i - nums[i])
        return res

    def missing_number_using_xor(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res

'''
Algorithm:

+-------+---+---+---+---+
| Index | 0 | 1 | 2 | 3 |
+-------+---+---+---+---+
| Value | 0 | 1 | 3 | 4 |
+-------+---+---+---+---+

missing = 4+(0-0)+(1-1)+(2-3)+(3-4)
        = 4 + 0 + 0 - 1 - 1 
        =2

Using XOR
  
missing = 4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
        = (4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
        =0∧0∧0∧0∧2
        =2
 '''
