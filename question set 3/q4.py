def max(a):
    m = a[0]
    for i in range(len(a)):
        if m < a[i]:
            m = a[i]
    return m

a = [1,2,3,1,4,5]
k = 3

a2 = []
x = 0
y = 0

while(x+1 < len(a)):
    for i in range(y,k+y):
        a2.append(a[i])
        x = i
    print(max(a2))
    a2 = []
    y += 1

    
