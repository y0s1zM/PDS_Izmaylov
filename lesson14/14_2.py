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

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is None:
            return node.value
        else:
            return self._find_min(node.left)

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right is None:
            return node.value
        else:
            return self._find_max(node.right)