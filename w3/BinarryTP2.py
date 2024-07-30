class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value <= root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root

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
my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)

# Preorder traversal
print("Preorder Traversal:", my_tree.preorder())

# Inorder traversal
print("Inorder Traversal:", my_tree.inorder())

# Postorder traversal
print("Postorder Traversal:", my_tree.postorder())