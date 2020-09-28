class Queue:
    SCALE_FACTOR = 2

    def __init__(self,capacity):
        self._entries = [None]*capacity
        self._head = self._tail = self._size = 0

    
    def __len__(self):
        return len(self._entries)

    def is_empty(self):
        return self.__len__() == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._entries[self._head]


    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._entries[self._head]
        self._entries[self._head] = None
        self._head = (self._head+1)%self.__len__()
        self._size -=1
        return answer


    def enqueue(self,e):
        if self._size == len(self._entries):
            self._resize(2*self.__len__())
        avail = (self._head+self._size)%len(self._entries)
        """The modulo is used to handle wrap around"""
        self._entries[avail] = e
        self._size+=1

    def _resize(self,cap):
        """Resize to a new list with capacity >=len(data)"""
        old = self._entries
        self._entries = [None]*cap
        old_front = self._head
        for k in range(self._size):
            self._entries[k]= old[old_front]
            old_front = (old_front+1)%len(old)
        self._head=0

