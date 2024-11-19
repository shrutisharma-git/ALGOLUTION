def left(a,ls,rs,p,q):
    while p > 0:
        ls -=1

# def right(a,ls,rs,p,q):
def equilibriumIndex(a):
    p = 0
    q = len(a) - 1
    ls,rs =0,0
    while p+1 != q-1:
        ls += a[p]
        rs += a[q]
        p += 1
        q -= 1
    
    left(a,ls,rs,p,q)
    right(a,ls,rs,p,q)

a = [-7,1,5,2,-4,3,0]