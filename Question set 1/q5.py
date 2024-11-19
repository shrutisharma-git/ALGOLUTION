def findNumber(a,key):
    for i in range(len(a)):
        if a[i] ==key:
            return i
    return -1

a = [1,2,4,23,4,21,5,5,6,5,4,10,4]
print(findNumber(a,int(input("Enter the number to find: "))))