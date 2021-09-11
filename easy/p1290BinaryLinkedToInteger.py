'''
Reference Link - https://www.youtube.com/watch?v=CyxbuJwA-0g
'''
from commons.LinkedList import Node


class SolutionDecimalToBinary:
    def get_decimal_value(self, node: Node) -> int:
        decimal_val = 0
        while node:
            decimal_val = decimal_val * 2 + node.val
            node = node.next
        return decimal_val

    def get_decimal_bitvector(self, node: Node) -> int:
        # multiplying by 1 is equivalent to left shifting
        decimal_val = 0
        while node:
            decimal_val = decimal_val << 1 | node.val
            node = node.next
        return decimal_val
