def left_shift_string(string, n):
    char_list = list(string)
    rotated_list = char_list[n:] + char_list[:n]
    rotated_string = "".join(rotated_list)
    return rotated_string


string=input("Enter the string:")
left_shift_string(string, 1)