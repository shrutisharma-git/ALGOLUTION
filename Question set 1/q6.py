def uniqueNumber(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    for i in d:
        if d[i] == 1:
            print(i,"is a unique number in array")

a = [1,1,2,2,3,5,3]
uniqueNumber(a)