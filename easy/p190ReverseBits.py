class SolutionReverseBits:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1  # extract the bits from start to end (0-31) by right shifting and &
            res = res | (bit << (31-i))  # insert the bits from end to start by left shifting and |

            # or operation is needed so that previous bits that are already should not be changed
        return res

# Time Complexity: O(1)
# Space Complexity: O(1)

