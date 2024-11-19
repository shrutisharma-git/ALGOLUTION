def parallelogram(r,c):
    x = r-1
    for i in range(c):
        y = x + r
        for i in range(y):
            if i < x:
                print(" ",end= " ")
            if i >= x:
                print("*",end = " ")
        print()
        x -= 1
r = 5
c = 4
parallelogram(r,c)