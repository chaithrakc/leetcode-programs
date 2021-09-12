import pytest

from medium.p423OriginalDigits import SolutionOriginalDigits

digits_test = [
    ('owoztneoer', '012'),
    ('fviefuro', '45')
]


class TestSolutionOriginalDigits:
    solution = SolutionOriginalDigits()

    @pytest.mark.parametrize('num_str, expected_str', digits_test)
    def test_original_digits(self, num_str: str, expected_str: str) -> None:
        assert self.solution.original_digits(num_str) == expected_str
