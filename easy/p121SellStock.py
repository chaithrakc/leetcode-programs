from typing import List


# we want to buy low and sell high
class SolutionSellStock:

    # Two Pointer Technique
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_index = 0
        for sell_index in range(1, len(prices)):
            if prices[sell_index] < prices[buy_index]:
                buy_index = sell_index  # buy index should always point to min price index
            else:
                profit = prices[sell_index] - prices[buy_index]
                max_profit = max(profit, max_profit)
        return max_profit
