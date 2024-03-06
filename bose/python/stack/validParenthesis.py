from StackV2 import Stack

class Solution:
    def __init__(self) -> None:
        self.stack = Stack()
        
    def pair_lookup(self,key):
        look_up = {
           "(":")",
        "{":"}",
        "[":"]"
        }
        return look_up.get(key,None)
    
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False
        for paranthesis in s:
            if self.pair_lookup(paranthesis):
                self.stack.push(paranthesis)
            elif self.stack.is_empty() or self.pair_lookup(self.stack.pop())!=paranthesis:
                return False
        if not self.stack.empty():
            return False
        return True
        
        
if __name__=="__main__":
    solution = Solution()
    s = "(("
    print(solution.isValid(s))