# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# Ryan Earl

class MaxHeap:
   def __init__(self): 
        self._data = []
        return None
   pass

   def _size(self): 
        return len(self._data)
