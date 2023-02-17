class SolutionHammingWeight:
    def hamming_weight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2 # mod with 2 to determine if last bit is 1 or 0
            n = n >> 1 # right shifting to get to the next bit
        return res

    def hamming_weight_optimized(self, n:int) -> int:
        res = 0
        while n>0:
            n &= (n-1)
            res += 1
        return res


# Time Complexity: we are guaranteed that every input is going to be 32 bit integer.
# While loop will be O(32) which is constant time.
# No matter what the input is, time complexity is not going to scale up
# So, its O(1)

# Space Complexity: O(1) ; no extra space

'''
Algorithm:
Example: 1011
1. how to know the last bit is 1/0? 
    a. using logical and operation: (1011) & (0001) = 0001 
    b. mod by 2: (1011) % 2
2. to check the next bit: shift the bits to right using >> operator
3. continue until the 'n' becomes 0 -> 00000000...0000 bits
'''

