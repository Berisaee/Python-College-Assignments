inp=input("Enter the comma separated sequence:")
strings=inp.split(sep=",")

def sort_print(list):
    strings.sort()
    print(strings)
    
sort_print(strings)