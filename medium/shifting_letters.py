# Difficulty : Medium

from typing import List


class Solution(object):
    def shifting_letters(self, s: str, shifts: List) -> str:
        ans = list()
        total_shifts = sum(shifts) % 26  # circular shift: if num of shifts goes beyond 27 (number of english alphabets)
        for index, letter in enumerate(s):
            alpha_index = ord(letter) - ord('a')
            ascii_val = chr(ord('a') + (alpha_index + total_shifts) % 26)
            ans.append(ascii_val)
            total_shifts = (total_shifts - shifts[index]) % 26  # curcular shift
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    result = solution.shifting_letters("ruu", [26, 9, 17])
    print(result)
