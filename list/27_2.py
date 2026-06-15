l1=list()
l2=list()

num=int(input("Enter the number of elements:"))
for i in range(num):
    x=str(input("Enter the element:"))
    l1.append(x)
print(l1)

for i in range(len(l1)):
    l2.append(l1[i][0])
    
print(l2)