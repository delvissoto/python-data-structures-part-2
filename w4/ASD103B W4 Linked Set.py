# Week 4 ASD103B 
# Delvis Soto

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedSet:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, value):
        if not self.contains(value):
            new_node = Node(value)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    def union(self, other_set):
        new_set = LinkedSet()
        current = self.head
        while current:
            new_set.add(current.value)
            current = current.next
        current = other_set.head
        while current:
            new_set.add(current.value)
            current = current.next

        return new_set
    def intersection(self, other_set):
        new_set = LinkedSet()
        current = self.head
        while current:
            if other_set.contains(current.value):
                new_set.add(current.value)
            current = current.next
        return new_set

set1 = LinkedSet()
set1.add(1)
set1.add(2)
set1.add(3)
set2 = LinkedSet()
set2.add(2)
set2.add(3)
set2.add(4)
print("Set 1 contains 2:", set1.contains(2))
print("Set 1 contains 5:", set1.contains(5)) 
set1.remove(2)
print("Set 1 after removing 2:", set1.contains(2)) 
union_set = set1.union(set2)
union_values = []
current = union_set.head
while current:
    union_values.append(current.value)
    current = current.next
print("Union of Set 1 and Set 2:", union_values) 
intersection_set = set1.intersection(set2)
intersection_values = []
current = intersection_set.head
while current:
    intersection_values.append(current.value)
    current = current.next
print("Intersection of Set 1 and Set 2:", intersection_values) 