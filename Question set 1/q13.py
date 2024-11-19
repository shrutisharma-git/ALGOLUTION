def numberPattern(n):
    for i in range(n):
        k = 5
        for j in range(n):
            if i%2 == 0:
                print(j+1,end=" ")
            else:
                print(k,end=" ")
            k-= 1

        print()

numberPattern(5)