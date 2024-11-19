def checkpal(a):
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            return False
    return True

def pal1(a):
    s = ""
    for i in range(len(a)):
        if (ord(a[i]) >= 65 and ord(a[i]) <= 90):
            s += chr(ord(a[i]) + 32)
        if (ord(a[i]) >= 97 and ord(a[i]) <= 122):
            s += a[i]
    print(s)
    return checkpal(s)


s = "A man, a plan, a canal; Panama"
print(pal1(s))