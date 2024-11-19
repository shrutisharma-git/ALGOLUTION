a = [10,100,1000]

ans = 0
for i in range(len(a)):
    ans = ans | a[i]
print(ans)