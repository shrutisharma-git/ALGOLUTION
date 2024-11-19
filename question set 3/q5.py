def paranthesis(s):
    stack = []
    top = -1

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
            top += 1
        elif s[i] == ")":
            if top == -1:
                return False
            else:
                stack.pop(top)
                top -= 1
    if top == -1:
        return True
    else:
        return False


s = "()(())()"
print(paranthesis(s))