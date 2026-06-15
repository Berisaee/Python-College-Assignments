list1=['xyz','abc','aba','2606']

new_list=[char for char in list1 if len(char)>2 and char[0]==char[-1]]
print(len(new_list))