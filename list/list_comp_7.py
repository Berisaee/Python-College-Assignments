import random

list1=list()
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))
for i in range(b):
    x=random.randint(a, b)
    list1.append(x)

print("Original list:",list1)

new_list=[pow(num,2) for num in list1 if pow(num,2)>50]

print("Required list:",new_list)