def countInversion(a):
    c = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                c+=1
    return c
a = [7,2,6,3]
print(countInversion(a))
            