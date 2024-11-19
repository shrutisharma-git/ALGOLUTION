def palindromeArray(a):
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            return False
    return True

def cyclic(s):
    if palindromeArray(s):
        return True
    a = []
    for i in range(len(s)):
        a.append(s[i])
    print(a)
    for i in range(len(s)-1):
        last = a[len(a)-1]
        for i in range(len(a)-2,-1,-1):
            a[i+1] = a[i]
        a[0] = last
        print(a)
        if palindromeArray(a):
            return True
    return False



s = "aaabbx"
print(cyclic(s))