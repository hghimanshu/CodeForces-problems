from Stack import Stack

def evaluate(RPN_expression):
    stack = Stack()
    DELIMETER = ","
    OPERATORS = {
        "+" : lambda x,y:x+y,
        "-" : lambda x,y:x-y,
        "*" : lambda x,y:x*y,
        "/" : lambda x,y:x/y
    }

    for i in RPN_expression.split(DELIMETER):
        if i not in OPERATORS:
            stack.push(int(i))
        else:
            stack.push(OPERATORS[i](stack.pop(),stack.pop()))
    return stack.pop()


if __name__ == "__main__":
    RPN = "3,4,+,2,*,1,+"
    print(evaluate(RPN))