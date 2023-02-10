import pytest

from easy.p231PowerofTwo import SolutionPowersOfTwo

power_of_two_test_cases = [
    (1,True),
    (16, True),
    (3, False)
]
class TestSolutionPowersOfTwo:
    solution = SolutionPowersOfTwo()

    @pytest.mark.parametrize('n, is_power_of_two',power_of_two_test_cases)
    def test_is_power_of_two(self, n:int, is_power_of_two:bool):
        assert self.solution.isPowerOfTwo(n) == is_power_of_two
