import pytest

from easy.p20ValidParentheses import SolutionValidParentheses

valid_parenthesis_tests = [
    ('()', True),
    ('()[]{}', True),
    ('(]', False)
]


class TestSolutionValidParentheses:
    solution = SolutionValidParentheses()

    @pytest.mark.parametrize('expression, is_valid', valid_parenthesis_tests)
    def test_is_valid(self, expression: str, is_valid: bool):
        assert self.solution.isValid(expression) == is_valid
