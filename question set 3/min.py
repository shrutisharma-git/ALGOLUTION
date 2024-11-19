def minStep(s):
    a = 0
    b = len(s)
    c = 0
    
    while a <= n and b >= -1:
        if s[a] == "1":
            s[a] = s[a+1]
            c+=1
        print(s,c)
    
s = "010"
n = len(s) 
print(minStep(ss))

 
