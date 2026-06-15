str="Sai Mangesh Beri"

list1=list(str[0],)
for i in range(len(str)):
    if str[i]==" ":
        list1.append(str[i+1])
    
new_str='.'.join(list1)
print(new_str)