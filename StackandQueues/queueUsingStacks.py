class queueWithStack:
    def __init__(self):
        self.stack = []
    

    def enqueue(self, x):
        self.stack.append(x)
    
    def dequeue(self):
        self.stack.pop(0)
    
    def getElements(self):
        print(self.stack)


obj = queueWithStack()
obj.enqueue(10)
obj.enqueue(1)
obj.enqueue(20)
obj.enqueue(6)
obj.enqueue(12)
obj.dequeue()
obj.getElements()