class queueWithStack:
    def __init__(self):
        self.enq, self.deq = [], []
    

    def enqueue(self, x):
        self.enq.append(x)
    
    def dequeue(self):
        if not self.deq:
            for _ in range(len(self.enq)):
                self.deq.append(self.enq.pop())
        return self.deq.pop()
                    
    
    def getElements(self):
        print(self.deq[::-1])


obj = queueWithStack()
obj.enqueue(10)
obj.enqueue(1)
obj.enqueue(20)
obj.enqueue(6)
obj.enqueue(12)
obj.dequeue()
obj.getElements()