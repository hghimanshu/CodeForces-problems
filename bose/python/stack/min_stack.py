from typing import List

class StackNode:
    def __init__(self,node_value,min_value) -> None:
        self.node_value = node_value
        self.min_value = min_value
        
    def min(self):
        return self.min_value
    
    def value(self):
        return self.node_value
    
    def __repr__(self) -> str:
        return f"Node: {self.node_value} | Min: {self.min_value}"

class MinStack:

    def __init__(self):
        self.container: List[StackNode] = []
        
    def is_empty(self):
        return len(self.container) == 0
        
    def push(self, val: int) -> None:
        if self.is_empty():
            self.container.append(StackNode(val,val))
        else:
            top_node = self.container[-1]
            last_min = top_node.min()
            print(f"Val is {val},last min is {last_min}")
            self.container.append(StackNode(val,min(val,last_min)))

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container.pop().value()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1].value()

    def getMin(self) -> int:
        return self.container[-1].min()
    
if __name__=="__main__":
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(-1)
    print(min_stack.getMin())
    min_stack.push(0)
    min_stack.push(3)
    min_stack.push(7)
    min_stack.push(-2)
    min_stack.push(4)
    print(min_stack.container)
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.pop())
    print(min_stack.getMin())