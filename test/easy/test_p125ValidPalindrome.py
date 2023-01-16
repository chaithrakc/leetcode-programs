import pytest

from easy.p125ValidPalindrome import SolutionValidPalindrome

valid_palindrome_test_cases = [
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
    (' ', True)
]


class TestSolutionValidPalindrome:
    solution = SolutionValidPalindrome()

    @pytest.mark.parametrize('input_str, is_palindrome', valid_palindrome_test_cases)
    def test_is_palindrome(self, input_str: str, is_palindrome: bool):
        assert self.solution.isPalindrome(input_str) == is_palindrome
