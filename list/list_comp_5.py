l1=[10,20,30]
l2=[30,10,40]

new_list=[(x,y) for x in l1 for y in l2 if x!=y]
print(new_list)