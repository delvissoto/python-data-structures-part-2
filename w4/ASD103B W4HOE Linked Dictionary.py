# Week 4 Hands On Exercise Linked Dictionary
# Delvis Soto

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class LinkedDict:
    def __init__(self):
        self.head = None
    def add(self, key, value):
        if not self.head:
            self.head = Node(key, value)
        else:
            current = self.head
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key, value)
    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def delete(self, key):
        current = self.head
        if current and current.key == key:
            self.head = current.next
            return
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
    def display(self):
        current = self.head
        while current:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next

linked_dict = LinkedDict()

linked_dict.add("a", 1)
linked_dict.add("b", 2)
linked_dict.add("c", 3)

linked_dict.display()

print("Value for key 'b':", linked_dict.get("b"))  
print("Value for key 'd':", linked_dict.get("d"))  

linked_dict.add("b", 20)
linked_dict.display()

linked_dict.delete("b")
linked_dict.display()