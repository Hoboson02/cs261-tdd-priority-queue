# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Ryan Earl

class NaivePriorityQueue:
    def __init__(self): 
        self.data = []
        return None
    pass

    def enqueue(self, value): 
        return self.data.append(value)

    def dequeue(self): 
        return self.data.pop()