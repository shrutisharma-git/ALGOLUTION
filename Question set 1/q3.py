def merge(a,b):
    c = [0]*(len(a)+len(b))
    p = 0
    q = 0
    k = 0
    while p < len(a) and q < len(b):
        if a[p] > b[q]:
            c[k] = b[q]
            q += 1
        elif a[p] <= b[q]:
            c[k] = a[p]
            p += 1
        k += 1
        print(c)

    while p < len(a):
        c[k] = a[p]
        k += 1
        p += 1
        print(c)
    while q < len(b):
        c[k] = b[q]
        k += 1
        q += 1
        print(c)

    return c

a = [1,2,4,5,9]
b = [5,6,7,10,13]
c = merge(a,b)
print(c)



