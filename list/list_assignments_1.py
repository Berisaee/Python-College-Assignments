def list_func(list):
    length=len(list[0])
    for i in range(len(list)):
        if(len(list[i])>length):
            length=len(list[i])
            print(list[i])
            
strings=["Python","Software","Programming","Language"]
list_func(strings)       