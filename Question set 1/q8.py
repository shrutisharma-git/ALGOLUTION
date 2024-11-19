def duplicateNumber(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    c = 0
    for i in d:
        if d[i] > 1:
            c += 1
    print("Number of duplicate in array are",c)
a= [1,2,3,2,2,1,2,1,2,16,7,79,9,0,0]
duplicateNumber(a)

