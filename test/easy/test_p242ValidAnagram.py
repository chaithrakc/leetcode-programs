import pytest

from easy.p242ValidAnagram import SolutionValidAnagram

valid_anagram_testcases = [
    ('anagram', 'nagaram', True),
    ('rat', 'car', False)
]


class TestSolutionValidAnagram:
    solution = SolutionValidAnagram()

    @pytest.mark.parametrize('input_str, anagram, is_anagram', valid_anagram_testcases)
    def test_is_anagram(self, input_str: str, anagram: str, is_anagram: bool):
        assert self.solution.is_anagram(input_str, anagram) == is_anagram
