string=input("Enter the string:")
upper=0
lower=0
digit=0
space=0

for char in string:
    if char.isupper():
        upper=upper+1
    elif char.islower():
        lower=lower+1
    elif char.isdigit():
        digit=digit+1
    elif char.isspace():
        space=space+1
        
print("Original String:",string)
print("Number of uppercase letters:",upper)
print("Number of lowercase letters:",lower)
print("Number of digits:",digit)
print("Number of whitespaces:",space)