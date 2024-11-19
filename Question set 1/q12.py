def diamond(n):
    if n%2 == 0:
        return False
    
    x ,y = n//2,n//2
    print("x,y",x,y)

    for i in range(n//2+1):
        for j in range(n):
            if j >= x and j <= y:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        x -= 1
        y += 1
        print()
    # print(x,y)
    x+=1
    y-=1
    for i in range(n//2):
        x += 1
        y -= 1
        for j in range(n):
            if j >= x and j <= y:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print(x,y)
diamond(7)