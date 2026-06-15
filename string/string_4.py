string=input("Enter a string:")
string_list=list(string)

string_list.reverse()

new_string=''.join(string_list)

print("Original list:",string)
print("Required list:",new_string)