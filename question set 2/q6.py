def abc(a,x):
    p =0
    q = len(a)-1

    while p < q:
        if a[p] + a[q] == x:
            print(a[p],a[q])
            return 
        elif a[p] + a[q] > x:
            q -= 1
        else:
            p += 1
    print(-1)

a = [1,2,4,5,7,11]
n = 6
x = 9
abc(a,x)