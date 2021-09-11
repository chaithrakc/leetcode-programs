import pytest

from commons.BinaryTree import BinaryTree
from easy.p572SubtreeofAnotherTree import SolutionSubtree

subtree_tests = [
    (BinaryTree(3, 4, 5, 1, 2, None, None, None, None, 0, None), BinaryTree(4, 1, 2), False),
    (BinaryTree(3, 4, 5, 1, 2), BinaryTree(4, 1, 2), True)
]


class TestSolutionSubtree:
    solution = SolutionSubtree()

    @pytest.mark.parametrize('tree, subtree, is_subtree', subtree_tests)
    def test_is_subtree(self, tree: BinaryTree, subtree: BinaryTree, is_subtree: bool) -> None:
        assert self.solution.is_subtree(tree.root, subtree.root) == is_subtree
