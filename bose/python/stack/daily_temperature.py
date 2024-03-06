from typing import List

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

class Solution:
    def __init__(self) -> None:
        self.stack =  Stack()
        self.answer = []
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        self.answer = [0 for i in range(len(temperatures))]
        self.stack.push((temperatures[0],0))
        
        for i in range(1,len(temperatures)):
            print(f"answer is :: {self.answer}")
            print(f"stack is :: {self.stack}")
            while not self.stack.is_empty():
                if temperatures[i] > self.stack.peek()[0]:
                    stack_top_temp,stack_top_idx = self.stack.pop()
                    self.answer[stack_top_idx] = i-stack_top_idx
                else:
                    break
            self.stack.push((temperatures[i],i))
        
        while not self.stack.is_empty():
            stack_top_temp,stack_top_idx = self.stack.pop()
            self.answer[stack_top_idx] = 0
        
        return self.answer
    

if __name__=="__main__":
    solution = Solution()
    temperatures = [30,60,90]
    print(solution.dailyTemperatures(temperatures=temperatures))
        