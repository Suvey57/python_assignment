def even_list(lists):
    new=[]
    for i in lists:
        if i%2==0:
            new.append(i)
    return(new)

l = list(map(int,input("Enter elements of list separated by space\n").split()))
print(even_list(l))
