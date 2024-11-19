def sw(a,k):
    s = 0
    for i in range(k):
        s += a[i]
    
    p = 0
    q = k-1
    ans = s
    arr = [0]*k
    while q < len(a)-1:
        s -= a[p]
        p += 1

        q += 1
        s += a[q]
        
        if s > ans:
            ans = s
            x = 0
            for i in range(p,q+1):
                arr[x] = a[i] 
                x+=1
            print(arr)
    return ans

a = [100,200,300,400]
k = 4

print(sw(a,k))