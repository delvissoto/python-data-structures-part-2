from LinkedQueue import LinkedQueue
def test():
    print("hello test")
    q = LinkedQueue()
    print(" Lenght: ", len(q))
    
    print("Is the queue empty", q.isEmpty())
    print("Adding 1 - 10")
    for i in range(10):
        q.add(i+1)
    print("What is peek?? ", q.peek)
    print("Clearing the queue now *****")
    q1 = LinkedQueue(q)
    print("Are q1 and q equal??" , q.__eq__(q1))
    q1.clear
    print("Content of cloned queue after clearing ", q1)
    print("How many times 1 occurs?? ", q.count(1))

test()