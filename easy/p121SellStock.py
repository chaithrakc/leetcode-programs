from typing import List


# we want to buy low and sell high
class SolutionSellStock:

    # Two Pointer Technique
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        left_ptr = 0 # buy low; should point to the lowest value at any point
        # right_ptr (sell high ; should point to the highest value at any point)
        for right_ptr in range(1, len(prices)):
            if prices[right_ptr] < prices[left_ptr]:
                left_ptr = right_ptr  # buy index should always point to min price index
            else:
                profit = prices[right_ptr] - prices[left_ptr]
                max_profit = max(profit, max_profit)
        return max_profit
