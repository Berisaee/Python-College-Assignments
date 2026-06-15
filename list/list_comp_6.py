sequence="the quick brown fox jumps over the lazy dog"
list1=sequence.split()
out=[len(word) for word in list1 if word!='the']
print(out)