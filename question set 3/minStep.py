def minStep(s):
    a = 0
    b = len(s)
    c = 0
    ans = 0
    
    for i in range(n-1,-1,-1):
        if s[a] == "1":
            s[a] = s[a+1]
            ans = s[a]
            c+=1
        return ans
    
s = "010"
n = len(s) 
print(minStep(s))

 
