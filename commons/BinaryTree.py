from typing import Any, List


class TreeNode:
    def __init__(self, val: Any, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class BinaryTree:
    root = None

    def __init__(self, *params):
        self.root = self.insert_levelorder(list(params), self.root, 0, len(params))

    def insert_levelorder(self, arr: List, cur_node: TreeNode, i: int, n: int) -> TreeNode:
        if i < n:
            temp = TreeNode(arr[i])
            cur_node = temp
            cur_node.left = self.insert_levelorder(arr, cur_node.left, 2 * i + 1, n)  # insert left child
            cur_node.right = self.insert_levelorder(arr, cur_node.right, 2 * i + 2, n)  # insert right child
        return cur_node

    # preorder
    def repr_helper(self, node: TreeNode, nodes: List):
        if node:
            nodes.append(str(node.val))
            self.repr_helper(node.left, nodes)
            self.repr_helper(node.right, nodes)

    # pre-order tranversal: root, left, right
    def __repr__(self) -> str:
        node = self.root
        nodes = list()
        self.repr_helper(node, nodes)
        return ','.join(nodes)
