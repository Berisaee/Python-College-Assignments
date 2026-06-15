def ceaser(text,shift):
    e_text=""
    for char in text:
        if char.isalpha():
            shifted_char=chr((ord(char.lower())-ord('a')+ shift)% 26 + ord('a'))
            if char.isupper():
                e_text+=shifted_char.upper()
            else:
                e_text+=shifted_char
        else:
            e_text+=char
    return e_text

text="abc"
shift=3
e_text=ceaser(text, shift)
print(f"Original text:{text}")
print(f"Encrypted text(shift {shift}):{e_text}")