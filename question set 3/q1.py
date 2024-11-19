def check(i):
    for x in range(1,i//2):
        if x*x == i:
            return False
    return True

a = 100
ans = 0
for i in range(1,a//2):
    if a%i == 0 and check(i):
        ans += 1
print(ans)