from typing import List


class BinarySearch:
    @staticmethod
    def binary_search(sorted_arr:List[int], key:int) -> int:
        left_ptr = 0
        right_ptr = len(sorted_arr) - 1
        while left_ptr<=right_ptr:
            mid_ptr = (left_ptr+right_ptr)//2 # floor division to avoid decimal index
            if sorted_arr[mid_ptr] == key:
                return mid_ptr # return index of the search element
            elif key >= sorted_arr[mid_ptr]:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1

        return -1 # if element is not found