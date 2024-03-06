class Stack:
    """Implementation of Stack in python
    """
    def __init__(self) -> None:
        self.container = []
    
    def is_empty(self):
        return len(self.container) == 0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container.pop()
    
    def push(self,value):
        self.container.append(value)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1]

    def flush(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        while not self.is_empty():
            self.container.pop()
            
    def __repr__(self) -> str:
        return ",".join(str(i) for i in self.container)
        

if __name__=="__main__":
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack.peek())
    print(stack.pop())
    stack.push(100)
    print(stack)
    stack.flush()
    stack.peek()