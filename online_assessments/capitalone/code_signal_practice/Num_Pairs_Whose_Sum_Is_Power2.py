"""
https://leetcode.com/discuss/interview-question/872882/quora-coding-challenge-number-of-pairs-whose-sum-is-a-power-of-2
https://www.geeksforgeeks.org/number-of-pairs-whose-sum-is-a-power-of-2-set-2/

Given an integer array, return the number of pairs of indices such that its array values sum to a power of 2.
For reference, powers of 2 are: 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16, etc...

This problem is modification of LeetCode Problem#1 Two Sum

Example:
a = [1, -1, 2, 3]
Output: 5
(0,0) = 1 + 1 = 2 (which is a power of 2)
(1,2) = -1 + 2 = 1 (which is a power of 2)
(1,3) = -1 + 3 = 2 (which is a power of 2)
(0,3) = 1 + 3 = 4 (which is a power of 2)
(2,2) = 2 + 2 = 4 (which is a power of 2)
Therefore, there are 5 pairs of indices whose array values sum is a power of 2 so the output is 5.

In case, you may not use the same element twice.
for loop will change:
```
    for i in range(31):
        target = 2 ** i
        prev_nums_set = set() # works because of commutative property of addition
        for num in numbers:
            diff = target - num
            if diff in prev_nums_set:
                count += 1
            prev_nums_set.add(num) # add it to the set after processing the current element to avoid using same
            element twice
    return count
```
"""
from typing import List


def solution(numbers:List[int]) -> int:
    count = 0
    for i in range(31):
        target = 2 ** i
        prev_nums_set = set() # works because of commutative property of addition
        for num in numbers:
            prev_nums_set.add(num)
            diff = target - num
            if diff in prev_nums_set:
                count += 1
    return count

# driver code
test_arr = [1, -1, 2, 3]
num_pairs = solution(test_arr)
print(num_pairs)

"""
The reason why the loop range is up to 31 is because we're checking if the sum of two numbers in the input array is 
a power of 2, and the highest power of 2 that can be represented by a 32-bit signed integer (which is what most 
programming languages use to represent integers) is 2^31. Therefore, we only need to check for powers of 2 up to 
2^30 to cover all possible sums that can be represented by two integers in the input array.
"""