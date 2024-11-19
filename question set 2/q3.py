def kthLargest(a,k):
    if k > len(a):
        return "Invalid"
    else:
        for i in range(k):
            max = 0 
            for j in range(1,len(a)):
                if a[max]<a[j]:
                    max = j
            ans = a[max]
            a[max] = float("-inf")
    return ans

a = [3,2,1,5,6,4]
k = int(input("Enter kth element : "))

print(kthLargest(a,k))