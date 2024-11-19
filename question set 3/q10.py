def insertion(a,val,i):
    a[i] = val
    while (i!=0 and a[(i-1)//2] > val):
        temp = a[(i-1)//2]
        a[(i-1)//2] = a[i]
        a[i] = temp

        i = (i-1)//2
    

def deletion(a,):



a = [11,8,5,7,5,100]
k = 4 