l1=list()
num=int(input("Enter the number of elements:"))
for i in range(num):
    x=int(input("Enter the element:"))
    l1.append(x)
print(l1)

l2=list()
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)