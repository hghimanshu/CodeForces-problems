from collections import deque

class circularQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.head = -1
        self.tail = -1
        self.queue = [None for i in range(self.maxSize)]
    
    def enqueue(self, x):
        if (self.tail +1) % self.maxSize == self.head:
            raise ValueError("Queue is fully filled")
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = x
        
        else:
            self.tail = (self.tail +1)% self.maxSize
            self.queue[self.tail] = x

    def dequeue(self):
        if self.head == -1:
            raise ValueError("Queue is empty")
        
        if self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head +1 )% self.maxSize
            return temp

    def getElements(self):
        print(self.queue)


ob = circularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.getElements() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.getElements() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.getElements() 