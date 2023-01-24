import pytest

from jpmc.Titles import SolutionTitles

titles_testcases = [
    ('Hello world', 'Hello World'),
    ('a letter in the mail', 'A Letter In The Mail'),
    ('a Letter', 'A Letter')
]


class TestSolutionTitles:
    solution = SolutionTitles()

    @pytest.mark.parametrize('text,title',titles_testcases)
    def test_generate_titles(self, text:str,title:str):
        assert self.solution.generate_titles(text) == title

    @pytest.mark.parametrize('text, title', titles_testcases)
    def test_cap_sentence(self, text:str,title:str):
        assert self.solution.generate_titles(text) == title
