import random

list1=list()
lower_bound=int(input("Enter the lower bound:"))
upper_bound=int(input("Enter the upper bound:"))
for i in range(upper_bound):
    x=random.randint(lower_bound, upper_bound)
    list1.append(x)

print("Original list:",list1)

def largest(list):
    list.sort()
    print("The largest number in the list is:",list[-1])
    
largest(list1)