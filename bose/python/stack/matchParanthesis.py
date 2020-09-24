from Stack import Stack
def matchParanthesis(expr):
    stack = []

    lookup = {
        "(":")",
        "{":"}",
        "[":"]"
    }

    for i in expr:
        if i in lookup:
            stack.append(i)
        elif not stack or lookup[stack.pop()]!=i:
            return False
    if len(stack)>0:
        return False
    return True

if __name__ == "__main__":
    # print(matchParanthesis("[(){()()}]"))
    print(matchParanthesis("("))

