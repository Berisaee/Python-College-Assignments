a=[10,20,30,20,10,50,60,40,80,50,40]

print("Original List:",a)
new_list=list()
for num in a:
    if num not in new_list:
        new_list.append(num)
        
print("Required list:",new_list)