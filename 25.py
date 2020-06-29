def empty_dictionary(lists):
    m=1
    for i in range(len(lists)):
        if len(lists[i])>0:
            m=0
            break
    if m==0:
        print("False")
    else:
        print("True")

empty_dictionary([{},{},{}])
empty_dictionary([{1,2},{},{}])
