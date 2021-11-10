import pytest

from easy.p1507ReformatDate import SolutionReformatDate

format_date_tests = {
    ('20th Oct 2052', '2052-10-20'),
    ('6th Jun 1933', '1933-06-06'),
    ('26th May 1960', '1960-05-26')
}


class TestSolutionReformatDate:
    solution = SolutionReformatDate()

    @pytest.mark.parametrize('date,formatted_date', format_date_tests)
    def test_reformat_date(self, date: str, formatted_date: str):
        assert self.solution.reformat_date(date) == formatted_date
