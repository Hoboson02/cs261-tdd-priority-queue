# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Ryan Earl

class NaivePriorityQueue:
    def __init__(self): 
        self.data = []
        return None
    pass

    def enqueue(self, value): 
        self.data.append(value)

    def dequeue(self): 
        if self.is_empty(): 
            return None 
        highest_priority = 0 
        priority = 0
        while priority < len(self.data): 
            if self.data[highest_priority] < self.data[priority]: 
                highest_priority = priority 
            priority = priority + 1
        return self.data.pop(highest_priority)

        
        



    def is_empty(self): 
        return len(self.data) == 0