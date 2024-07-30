class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        self.root = self._add_node(self.root, value)

    def _add_node(self, root, value):
        if root is None:
            return Node(value)
        if value <= root.value:
            root.left = self._add_node(root.left, value)
        else:
            root.right = self._add_node(root.right, value)
        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        elif value < root.value:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, root):
        if root is None:
            return []
        result = [root.value]
        result += self._preorder(root.left)
        result += self._preorder(root.right)
        return result

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            return []
        result = self._inorder(root.left)
        result.append(root.value)
        result += self._inorder(root.right)
        return result

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, root):
        if root is None:
            return []
        result = self._postorder(root.left)
        result += self._postorder(root.right)
        result.append(root.value)
        return result

# Test cases
my_tree = BinaryTree()

# Adding nodes
my_tree.add_node(5)
my_tree.add_node(3)
my_tree.add_node(7)
my_tree.add_node(2)
my_tree.add_node(4)
my_tree.add_node(6)
my_tree.add_node(8)

# Searching for nodes
print("Is 4 in the tree?", my_tree.search(4))
print("Is 9 in the tree?", my_tree.search(9))

# Preorder traversal
print("\nPreorder Traversal:", my_tree.preorder())

# Inorder traversal
print("Inorder Traversal:", my_tree.inorder())

# Postorder traversal
print("Postorder Traversal:", my_tree.postorder())
