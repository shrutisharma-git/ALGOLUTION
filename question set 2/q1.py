def maxSumSubstring(a):
    p = 0
    q = 0
    ans = 0
    sum = 0
    while q < len(a):
        sum += a[q]
        if sum <= 0:
            p = q + 1
            sum = 0
        elif sum > ans:
            ans = sum
        q += 1
    return ans

a = [-1,2,-3,4,-1,2,1,-5,4]
print(maxSumSubstring(a))

