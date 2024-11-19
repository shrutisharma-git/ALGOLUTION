def majorityDict(a):
    d = {}
    c = 0
    f = 1
    for i in a:
        c+=1
        if i in d:
            d[i]+=1
            if d[i] >= len(a)//2:
                print(i)
                f = 0
                break
        else:
            d[i] =1

    if f==1:
        print(-1)
    print(c)

def majority(a): 
    x = 0
    for i in range(len(a)):
        x += 1
        c = 1
        if a[i] != None:
            for j in range(1+i,len(a)):
                x += 1
                if a[i] == a[j]:
                    a[j] = None
                    c += 1
        print(a)
        if c >= len(a)//2:
            print(a[i])
            break
    print(x)

a = [1,1,1,6,6,5,3,6,6,11,6]
majority(a)
