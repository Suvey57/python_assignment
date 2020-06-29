def first_and_last(lists):
    count = 0
    for i in lists:
        if len(i)>=2 and i[0]==i[-1]:
            count = count + 1
    print(count)
lists = list(input("Enter the elements of list:: ").split())
first_and_last(lists)
