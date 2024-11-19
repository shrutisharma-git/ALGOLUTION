def checkPairs(l):
    dict = {
        0 : 2,
        1 : 2,
        2 : 1,
        3 : 2,
        4 : 2,
        5 : 2,
        6 : 1,
        7 : 2,
        8 : 2,
        9 : 2
    }

    d = 0
    for i in range(len(l)):
        d += dict[l[i]]
    
    return (d)

l = [1,2,3,4,5]
print(checkPairs(l))