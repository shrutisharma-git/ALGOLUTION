def print(a,n):
 #10, 5, 3, 4, 1, 11
        m = 0
        i=0
        while(i!=0 and x<(a[(i-1)/2])):   
                x = (i-1)/2      
                m = x
                print(x,a[i],m)

a = []
n = int(input("Enter the number of elements :"))
for i in range(n):
    x = a.append(int(input("Enter a number to insert:")))
    y = print(a,n)
    print(y)