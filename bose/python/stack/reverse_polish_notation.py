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
        self.operator_functions = {
            "+": lambda x,y:x+y,
            "-": lambda x,y:x-y,
            "/": lambda x,y:x/y,
            "*": lambda x,y:x*y
        }
        self.rpn_stack = Stack()
        
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)<1:
            raise ValueError("Invalid token list")
        for token in tokens:
            if self.operator_functions.get(token,None):
                if self.rpn_stack.is_empty():
                    raise ValueError("Invalid token list")
                operand2 = self.rpn_stack.pop()
                operand1 = self.rpn_stack.pop()
                print(f"Operand 2 is {operand2}")
                print(f"Operand 1 is {operand1}")
                output = int(self.operator_functions.get(token)(operand1,operand2))
                self.rpn_stack.push(output)
                print(f"Token was :: {token} and output was {output}")
            else:
                self.rpn_stack.push(int(token))
            print(f"Token was :: {token}")
        return output
                
if __name__=="__main__":
    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(solution.evalRPN(tokens=tokens))