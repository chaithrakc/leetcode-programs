from jpmc.CheckSum import SolutionCheckSum
import pytest

check_sum_tests = [
    ('4388576018402626', 75),
    ('4388576018402625', 74),
    ('4388576018410707', 70),
]

valid_card_tests = [
    ('4388576018402626', False),
    ('4388576018402625', False),
    ('4388576018410707', True),
]

class TestSolutionCheckSum:
    solution = SolutionCheckSum()

    @pytest.mark.parametrize('card_num, check_sum',check_sum_tests)
    def test_find_check_sum(self, card_num:str, check_sum:int):
        assert self.solution.find_check_sum(card_num) == check_sum

    @pytest.mark.parametrize('card_num, is_valid',valid_card_tests)
    def test_valid_card(self, card_num:str, is_valid:bool):
        assert self.solution.valid_card(card_num) == is_valid
