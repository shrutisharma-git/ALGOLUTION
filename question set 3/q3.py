def checkParanthesis(a):
    stack = [0]*len(a)
    top = -1

    for i in range(len(a)):
        if a[i] == "{" and a[i] == "(" and a[i] == "[":
            top += 1
            stack[top] = a[i]
        else:
            if top == -1:
                return False
            if a[i] == ")" and stack[top] == "(":
                top -= 1
            elif a[i] == "]" and stack[top] == "[":
                top -= 1
            elif a[i] == "}" and stack[top] == "{":
                top -= 1
            else:
                return False
        if top == -1:
            return True
        return False


a = "(){}[]"
print(checkParanthesis(a))