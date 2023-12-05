import heapq  

class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.index = 0 
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index +=1 

    def pop(self):
        return heapq.heappop(self.queue)[-1]

pq = PriorityQueue()
pq.push("task1", 3)
pq.push("task3", 1)
pq.push("task3", 2)

print(pq.pop())
print(pq.pop())
print(pq.pop())