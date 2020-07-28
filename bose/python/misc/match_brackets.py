from stack_class import ArrayStack

def match_brackets(expr):
    brack_stack = ArrayStack()
    lefty = "({["
    righty = ")}]"

    for c in expr:
        if c in lefty:
            brack_stack.push(c)
        elif c in righty:
            if brack_stack.is_empty():
                return False
            if righty.index(c)!=lefty.index(brack_stack.pop()):
                return False
    return True


expr = "{(5+2)*(2+7)}"
print(match_brackets(expr))
