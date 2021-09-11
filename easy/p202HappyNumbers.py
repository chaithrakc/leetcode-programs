# Difficulty: Easy
class Solution(object):

    def get_next(self, n) -> int:
        total_sqr = 0
        while n > 0:
            n, rem = divmod(n, 10)
            total_sqr += rem ** 2
        return total_sqr

    def ishappy(self, n: int) -> bool:
        unique_sum = set()
        while n != 1 and n not in unique_sum:
            unique_sum.add(n)
            n = self.get_next(n)
        return n == 1

    # Floyds Algorithm to detect the cycle
    def ishappy_floyd(self, n: int) -> bool:
        fast_runner = self.get_next(n)
        slow_runner = n
        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))
        return fast_runner == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.ishappy(19))
    print(solution.ishappy_floyd(19))
