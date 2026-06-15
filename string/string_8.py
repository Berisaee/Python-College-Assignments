def rotate_string(s):
    for i in range(len(s)):
        print(s[i:]+s[:i])
    print(s)
    
rotate_string("SHIFT")