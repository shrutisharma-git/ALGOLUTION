def numberpattern(n):
    for i in range(n):
        print("1",end=" ")
    print()

    for i in range(n-2):
        for j in range(n):
            if j ==0 or j == n-1:
                print("1",end=" ")
            else:
                print(0,end=" ")
        print()

    for i in range(n):
        print("1",end=" ")
    print()
    

numberpattern(10)