l1=list()
num=int(input("Enter the number of elements:"))
for i in range(num):
    x=int(input("Enter the element:"))
    l1.append(x)
print(l1)
num1=int(input("Enter the element to be searched:"))
print("The index at which "+str(num1)+" is:")

count=0

for i in range(len(l1)):
    if num1==l1[i]:
        count=count+1
        print(i+1)
        
print("The element "+str(num1)+" is repeated for "+str(count)+" times")