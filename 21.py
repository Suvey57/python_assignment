def sort_tuples(lists):
    new_list=[]
    rev_list = []
    for i in range(len(lists)):
        rev_tuple = lists[i][::-1]
        rev_list.append(rev_tuple)
    rev_list.sort()
    for i in range(len(rev_list)):
        new_tuple = rev_list[i][::-1]
        new_list.append(new_tuple)
    print("reverse list is :: ",new_list)

l = []
line = input("enter tuples\n")
while(line!=""):
    l.append(tuple(line.split()))
    line = input()
sort_tuples(l)
