def removeElement(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k] = nums[i]
            k+=1
    ans = 0
    while k<len(nums):
        if nums[k]!=val:
           ans = nums[k] 
            
    return k, ans
    
nums = [0,1,2,2,3,0,4,2]
val = 2
result = removeElement(nums,val)
print(result)