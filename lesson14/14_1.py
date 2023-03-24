class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add_node(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self._add_node(value, node.right)
            else:
                node.right = TreeNode(value)

    def add_from_list(self, lst):
        for value in lst:
            if not isinstance(value, int):
                raise ValueError("Only integers can be added to the tree.")
            self.add_node(value)