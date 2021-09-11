from commons.LinkedList import LinkedList
from easy.p1290BinaryLinkedToInteger import SolutionDecimalToBinary
import pytest

decimal_linkedlist = [
    (LinkedList(1, 0, 1), 5),
    (LinkedList(1, 0, 1, 1, 0), 22),
    (LinkedList(1, 0, 1, 1), 11),
    (LinkedList(1, 1, 0, 1, 1), 27),
    (LinkedList(1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0), 18880)
]


class TestSolutionDecimalToBinary:
    solution = SolutionDecimalToBinary()

    @pytest.mark.parametrize("linkedlist, expected_decimal", decimal_linkedlist)
    def test_get_decimal_value(self, linkedlist: LinkedList, expected_decimal: int) -> None:
        assert self.solution.get_decimal_value(linkedlist.head) == expected_decimal

    @pytest.mark.parametrize("linkedlist, expected_decimal", decimal_linkedlist)
    def test_get_decimal_bitvector(self, linkedlist: LinkedList, expected_decimal: int) -> None:
        assert self.solution.get_decimal_bitvector(linkedlist.head) == expected_decimal
