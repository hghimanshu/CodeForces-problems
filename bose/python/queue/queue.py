class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def first(self):
        """ Return but do not remove the element at the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e FIFO)"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%self.__len__()
        self._size-=1
        return answer

    def enqueue(self):
        if self._size == len(self._data):
            self._resize(2*self.__len__())
        avail = (self._front + self._size)%len(self._data) 
        """The modulo is used in order to take care of the wrap around for the cicular queue"""
        self._data[avail] = e
        self._size +=1

    def _resize(self,cap):
        """Resize to a new list of capacity >= len(self._data)"""
        old = self._data
        self._data = [None]*cap
        old_front = self._front
        for k in range(self._size):
            self._data[k] = old[old_front]
            old_front = (old_front+1)%len(old)
        self._front = 0

        
    
