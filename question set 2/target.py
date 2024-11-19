def temp(a,n,t):
    maxlen = 0
    # sum, crrsum

    for i in range(n):
        sum = 0 
        crrlen = 0

        for j in range(i,n):
            sum+=a[j]
            if sum==t:
                crrlen = j+i-i
            elif crrlen > maxlen:
                maxlen = crrlen

    print(maxlen)
    print(crrlen)
    print(sum)
    print(n)

a = [5,6,-5,5,3,-2]
target = 8
n = len(a)
p = temp(a,n,target)
