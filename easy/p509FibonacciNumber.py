class SolutionFibonacci:
    # recursion : Slowest way to solve fibonacci sequence
    # Time complexity: O(2^N)
    # Space complexity: O(N)
    def fib(self, the_num: int) -> int:
        if the_num <= 1:
            return the_num
        return self.fib(the_num - 1) + self.fib(the_num - 2)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def fib_iterative(self, fib_value_at_index: int) -> int:
        prev1 = 0  # fib(0)
        prev2 = 1  # fib(1)
        fib_number = 0
        for num in range(fib_value_at_index):
            fib_number = prev2 + prev1
            prev1, prev2 = prev2, fib_number
        return prev1
