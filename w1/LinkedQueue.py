from abstractcollection import AbstractCollection
from node import Node
class linkedQueue(AbstractCollection):
    def  __inti__(self, sorceCollection):
        self.fron = None
        self.rear = None
        AbstractCollection.__init__(self, sorceCollection)
        
    def __iter__(self):
        cursor = self.front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
        
    def peek(self):
        if self.isEmpty():
            raise KeyError("The queue is empty")
        return self.front.data
    
    def clear(self):
        self.size = 0
        self.front = None
        self.rear = None
    
    def add(self, item):
        newNode = Node(item, None)
        if self.isEmpty():
            self.front = newNode
        self.rear +=1
            
    
 