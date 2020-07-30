class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if len(self.stack) == 0:
            print("Cant pop an empty stack!!")
            return None
        else:
            return self.stack.pop()
    
    def processResults(self, num1, num2, exp):
        if exp == "+":
            return num1 + num2
        elif exp == "-":
            return num1 - num2
        elif exp == "x":
            return num1 * num2
        elif exp == "/":
            return num1 // num2
    
    def processRPN(self, s):
        for i in s:
            if i in ["+","-", "x","/"]:
                value2 = self.pop()
                value1 = self.pop()
                res = self.processResults(value1, value2, i)
                self.push(res)

            else:
                self.push(int(i))
    
    def getAnswer(self):
        return self.stack



s = "34+2x1+"
ans = Stack()
ans.processRPN(s)
print(ans.getAnswer())