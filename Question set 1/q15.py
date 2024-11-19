def numberpattern(n):
    for i in range(n):
        c = i+1
        for j in range(n):
            # c = j+x
            # if c > 5:
            #     c = 5
            print(c,end=" ")
            if c < 5:
                c += 1

        print()


numberpattern(5)