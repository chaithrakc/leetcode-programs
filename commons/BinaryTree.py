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
        for item in params:
            self.insert(item)

    def __insert_helper(self, cur_node: TreeNode, data: Any) -> TreeNode:
        if not cur_node:
            return TreeNode(data)
        if data < cur_node.val:
            cur_node.left = self.__insert_helper(cur_node.left, data)
        elif data > cur_node.val:
            cur_node.right = self.__insert_helper(cur_node.right, data)
        else:
            return cur_node  # value already exists
        return cur_node

    def insert(self, data: Any):
        self.root = self.__insert_helper(self.root, data)

    def repr_helper(self, node: TreeNode, nodes: List):
        if node:
            nodes.append(str(node.val))
            self.repr_helper(node.left,nodes)
            self.repr_helper(node.right,nodes)

    # pre-order tranversal: root, left, right
    def __repr__(self) -> str:
        node = self.root
        nodes = list()
        self.repr_helper(node, nodes)
        return ','.join(nodes)
