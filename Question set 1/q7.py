def freqNumber(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in d:
        print("the frequency of number",i,"is",d[i])
a= [1,2,3,2,2,1,2,1,2,16,7,79,9,0]
freqNumber(a)

