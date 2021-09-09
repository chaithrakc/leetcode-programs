from typing import List

from commons.linked_list import Node, LinkedList


class Solution:
    def reverese_list(self, node: Node, num_list: List) -> None:
        if not node:
            return None
        self.reverese_list(node.next, num_list)
        num_list.append(node.data)

    # Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
    def get_decimal_value(self, node: Node) -> int:
        nums_list = list()
        self.reverese_list(node, nums_list)
        decimal_val = 0
        for index in range(len(nums_list)):
            decimal_val += 2 ** index * nums_list[index]
        return decimal_val


if __name__ == '__main__':
    solution = Solution()
    linkedList = LinkedList(1, 0, 1)
    result = solution.get_decimal_value(linkedList.head)
    print(result)
    linkedList = LinkedList(1, 0, 1,1,0)
    result = solution.get_decimal_value(linkedList.head)
    print(result)
    linkedList = LinkedList(1, 0, 1,1)
    result = solution.get_decimal_value(linkedList.head)
    print(result)
    linkedList = LinkedList(1,1, 0,1, 1)
    result = solution.get_decimal_value(linkedList.head)
    print(result)
