class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            return

        # Search for the node to be deleted
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # If the node is not found
        if not current:
            return

        # Unlink the node from the linked list
        prev.next = current.next

    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Test cases
my_linked_list = LinkedList()

# Adding nodes
my_linked_list.add_node(1)
my_linked_list.add_node(2)
my_linked_list.add_node(3)

# Printing the list
print("Original Linked List:")
my_linked_list.print_list()

# Inserting at the beginning
my_linked_list.insert_at_beginning(0)
print("\nLinked List after inserting at the beginning:")
my_linked_list.print_list()

# Deleting a node
my_linked_list.delete_node(2)
print("\nLinked List after deleting node with data 2:")
my_linked_list.print_list()

# Searching for a node
print("\nIs node with data 3 in the linked list?", my_linked_list.search_node(3))
print("Is node with data 5 in the linked list?", my_linked_list.search_node(5))
