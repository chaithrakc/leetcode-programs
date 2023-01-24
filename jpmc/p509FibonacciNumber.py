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
    def fib_iterative(self, the_num: int) -> int:
        if the_num <= 1:
            return the_num
        prev1 = 0  # fib(0)
        prev2 = 1  # fib(1)
        current = 0
        for num in range(2, the_num + 1):  # range is exclusive of the end term, we need to put the_num + 1
            current = prev2 + prev1
            prev2, prev1 = current, prev2
        return current