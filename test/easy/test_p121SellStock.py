from typing import List

import pytest

from easy.p121SellStock import SolutionSellStock

stock_tests = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([7, 5, 3, 3, 4], 1),
    ([7, 5, 3, 3, 3], 0),
    ([1], 0),
    ([], 0),
    ([1, 2], 1),
    ([7, 1, 5, 3, 6, 4, 0, 8], 8)
]


class TestSolutionSellStock:
    soultion = SolutionSellStock()

    @pytest.mark.parametrize('prices, sell_day', stock_tests)
    def test_max_profit(self, prices: List, sell_day: int) -> None:
        assert self.soultion.max_profit(prices) == sell_day
