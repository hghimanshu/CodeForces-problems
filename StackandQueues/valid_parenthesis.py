s = "[()[]{(}]"
stack = []

for i in s:
    if i in ["[", "(", "{"]:
        stack.append(i)
    else:
        if i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
        elif i == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)

if len(stack) == 0:
    print("Valid parenthesis !!")
else:
    print("Invalid parenthesis !!")