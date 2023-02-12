import pytest

from easy.p509FibonacciNumber import SolutionFibonacci

fib_test = [
    (2, 1),
    (3, 2),
    (4, 3)
]


class TestSolutionFibonacci:
    solution = SolutionFibonacci()

    @pytest.mark.parametrize('num, fib_number', fib_test)
    def test_fib(self, num: int, fib_number: int) -> None:
        assert self.solution.fib(num) == fib_number

    @pytest.mark.parametrize('num, fib_number', fib_test)
    def test_fib_iterative(self, num: int, fib_number: int) -> None:
        assert self.solution.fib_iterative(num) == fib_number

