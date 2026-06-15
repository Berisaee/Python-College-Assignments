def long_words(n,str):
    str=str.split()
    new_list=[char for char in str if len(char)>n]
    print(new_list)
    
    
long_words(3, "The quick brown fox jumps over the lazy dog")