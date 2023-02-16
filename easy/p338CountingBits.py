from typing import List


class SolutionCountBits:
    def count_bits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


'''
Pattern:
offset = 1, 2, 4, 8, 16, 32 .... powers of 2
0 will be the base case

+----+--------+--------+----------------+
| n  | offset | binary |   dp pattern   |
+----+--------+--------+----------------+
|  0 |      0 |   0000 | base condition |
|  1 |      1 |   0001 | 1+dp[1-1] = 1  |
|  2 |      2 |   0010 | 1+dp[2-2] = 1  |
|  3 |      2 |   0011 | 1+dp[3-2] = 2  |
|  4 |      4 |   0100 | 1+dp[4-4] = 1  |
|  5 |      4 |   0101 | 1+dp[5-4] = 2  |
|  6 |      4 |   0110 | 1+dp[6-4] = 2  |
|  7 |      4 |   0111 | 1+dp[7-4] = 3  |
|  8 |      8 |   1000 | 1+dp[8-8] = 1  |
|  9 |      8 |   1001 | 1+dp[9-8] = 2  |
| 10 |      8 |   1010 | 1+dp[10-8] = 2 |
+----+--------+--------+----------------+
 
'''
