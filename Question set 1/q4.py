def reverse(a):
    for i in range(len(a)//2):
        temp = a[i]
        a[i] = a[-i-1]
        a[-i-1] = temp
    return a

def palindromeArray(a):
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            return False
    return True

a = []
for i in range(7):
    a.append(int(input("Enter the number: ")))
r = reverse(a)
print("After reversing the order ",r)