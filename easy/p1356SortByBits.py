from typing import List


class SolutionSortByBits:
    def sort_by_bits(self, arr: List[int]) -> List[int]:
        # sort by number of 1s and then by the values
        return sorted(arr, key=lambda the_num: (bin(the_num).count('1'), the_num))
