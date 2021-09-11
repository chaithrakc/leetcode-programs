class SolutionFibonacci:
    def fib(self, the_num: int) -> int:
        if the_num <= 1:
            return the_num
        return self.fib(the_num - 1) + self.fib(the_num - 2)
