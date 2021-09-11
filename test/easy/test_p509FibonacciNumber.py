import pytest

from easy.p509FibonacciNumber import SolutionFibonacci

fib_test = [
    (2, 1),
    (3, 2),
    (4, 3)
]


class TestSolutionFibonacci:
    solution = SolutionFibonacci()

    @pytest.mark.parametrize('num, exepcted_sum', fib_test)
    def test_fib(self, num: int, exepcted_sum: int) -> None:
        assert self.solution.fib(num) == exepcted_sum
