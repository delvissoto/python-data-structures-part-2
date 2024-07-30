class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value <= current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value) if self.root else False

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value if current else None

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value if current else None

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp = self._min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursive(current_node.right, temp.value)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current_node):
        if current_node is None:
            return -1
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return max(left_height, right_height) + 1
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_recursive(current_node.right, result)

bst = BinaryTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("Search for 5:", bst.search(5))
print("Search for 20:", bst.search(20))

print("Minimum value:", bst.find_min())

print("Maximum value:", bst.find_max())

bst.delete(5)
print("After deleting 5:", bst.inorder())

print("Height of the tree:", bst.height())