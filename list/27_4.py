import random
l1=list()
even=list()
odd=list()
num1=int(input("Enter the starting number:"))
num2=int(input("Enter the ending number:"))
for i in range(num2):
    x=random.randint(num1,num2)
    l1.append(x)

print(l1)

for i in l1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
        
print("Even List:"+str(even))
print("Odd List:"+str(odd))