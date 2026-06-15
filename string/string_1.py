string=input("Enter the string:")
print("Given string:",string)

vowel_count=0
for char in string:
    if char in 'aeiou':
        vowel_count=vowel_count+1

print("The number of vowels in your string are ",vowel_count)        