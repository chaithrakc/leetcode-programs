import pytest

from medium.p91DecodeWays import SolutionDecodeWays

decode_tests = [
    ('12', 2),
    ('226', 3),
    ('11106', 2),
    ('0', 0),
    ('06', 0),
    ('20', 1),
    ('60', 0),
    ('909', 0),
    ('109', 1),
    ('2125', 5)
]


class TestSolutionDecodeWays:
    solution = SolutionDecodeWays()

    @pytest.mark.parametrize('encoded_str, num_ways', decode_tests)
    def test_num_decodings(self, encoded_str: str, num_ways: int) -> None:
        assert self.solution.num_decodings(encoded_str) == num_ways
