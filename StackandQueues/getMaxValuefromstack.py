class Stack:
    def __init__(self):
        self.stack = []
    

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        self.stack.pop()
    
    def maxValue(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        return max(self.stack)
    
    def printStack(self):
        return self.stack


l = Stack()
l.push(32)
l.push(2)
l.push(7)
print(l.printStack())
l.pop()
print(l.printStack())
print(l.maxValue())
