import collections

class Queue:
    def __init__(self):
        self._data = collections.deque()

    def __len__(self):
        return len(self._data)
        
    def enqueue(self,x):
        self._data.append(x)

    
    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)