class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.size() < 1:
            return None
        else:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue("apple")
    my_queue.enqueue("app")
    my_queue.enqueue("pear")
    my_queue.enqueue("banana")
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.size())
            
            class MyIterator:
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < 5:
            result = self.counter
            self.counter += 1
            return result
        else:
            raise StopIteration

# Using the iterator
my_iterator = MyIterator()
iter_obj = iter(my_iterator)

for item in iter_obj:
    print(item)