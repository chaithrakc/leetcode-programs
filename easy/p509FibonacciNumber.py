class SolutionFibonacci:
    # Time complexity: O(2^N)
    # Space complexity: O(N)
    def fib(self, the_num: int) -> int:
        if the_num <= 1:
            return the_num
        return self.fib(the_num - 1) + self.fib(the_num - 2)