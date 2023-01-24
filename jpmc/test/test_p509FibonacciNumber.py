import pytest

from jpmc.p509FibonacciNumber import SolutionFibonacci

fib_test = [
    (2, 1),
    (3, 2),
    (5, 5),
    (12, 144),
    (4, 3)
]
class TestSolutionFibonacci:
    solution = SolutionFibonacci()

    @pytest.mark.parametrize('num, expected_sum', fib_test)
    def test_fib(self, num: int, expected_sum: int) -> None:
        assert self.solution.fib(num) == expected_sum

    @pytest.mark.parametrize('num, expected_sum', fib_test)
    def test_fib_iterative(self, num: int, expected_sum: int) -> None:
        assert self.solution.fib_iterative(num) == expected_sum

