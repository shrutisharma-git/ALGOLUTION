# 
a= []
max = int(input("Enter the number: "))
a.append(max)
for i in range(4):
    x = int(input("Enter the number: "))
    a.append(x)
    if max < x:
        max = x
print("the maximum number is",max)