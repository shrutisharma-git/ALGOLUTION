def insert(a,val,i):
    a[i] = val
    while (i!=0 and a[(i-1)//2] < val):
        temp = a[(i-1)//2]
        a[(i-1)//2] = a[i]
        a[i] = temp

        i = (i-1)//2

n = int(input("Enter the number of element to insert : ")) 
a = [0]*n
for i in range(n):
    val = int(input("Enter the value to insert : "))
    insert(a,val,i)
    print(a)