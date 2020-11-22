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

     def _is_empty(self): 
        return len(self._data) == 0 

     def _last_index(self): 
          return len(self._data) -1
     
     def _value_at(self, value): 
          if 0 <= value <= self._size(): 
               return self._data[value]
          else: raise IndexError

     def _left_child_index(self, value): 
          return 2 * value + 1

     def _right_child_index(self, value): 
          return 2 * value + 2

     def _parent_index(self, value): 
          return (value -1) // 2

     def _parent(self, value): 
          return self._value_at(self._parent_index(value))

     def _left_child(self, value): 
          if self._size() < self._left_child_index(value): 
               return None
          elif self._size() > self._left_child_index(value): 
               return self._data[self._left_child_index(value)]

     def _right_child(self, value): 
          if self._size() < self._right_child_index(value): 
               return None
          elif self._size() > self._right_child_index(value): 
               return self._data[self._right_child_index(value)]

     def _has_right_child(self, value): 
          if self._right_child(value) !=None:
               return True
     def _has_left_child(self, value):
          if self._left_child(value) !=None:
               return True

     def _greater_child_index(self, value): 
          if self._right_child is None and self._left_child is None:
               return None
          elif self._has_left_child != None: 
               return self._has_left_child(value)