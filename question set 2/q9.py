def maxProfit(a):
    b = 0
    s = 1
    ans = a[s] - a[b]
    while s < len(a):
        if a[b] >= a[s]:
            b = s
        elif a[b] < a[s]:
            x = a[s] - a[b]
            if ans < x:
                ans = x
        s += 1
    return ans
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
