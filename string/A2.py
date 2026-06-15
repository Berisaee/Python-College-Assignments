def remove_char(inp):
    result=[]
    for char in inp:
        if char not in result:
            result.append(char)
    return ''.join(result)

inp_str="Deccan Education Society"
print(remove_char(inp_str))