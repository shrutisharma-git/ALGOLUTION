# print the number of negative elements in array
def findNeg(a):
    c = 0
    for i in a:
        if i < 0:
            c += 1
    return c

a = [1,1,2,3,3,2,2,-1,-2]
print(findNeg(a))
