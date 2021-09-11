from typing import Optional

from commons.BinaryTree import TreeNode


class SolutionSubtree:
    def is_subtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isidentical(root, subroot): return True
        return self.is_subtree(root.left, subroot) or self.is_subtree(root.right, subroot)

    def isidentical(self, tree: TreeNode, subtree: TreeNode):
        if not tree and not subtree: return True
        if not tree or not subtree: return False
        if tree.val != subtree.val: return False
        return tree.val == subtree.val \
               and self.isidentical(tree.left, subtree.left) \
               and self.isidentical(tree.right, subtree.right)
