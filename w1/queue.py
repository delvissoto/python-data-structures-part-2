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
            
            