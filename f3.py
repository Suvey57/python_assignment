def mul(b):
    mul=1
    for i in range(len(b)):
        mul=mul*b[i]
    return(mul)

n=int(input("enter numbers of elements to be inputted in the list:"))
a=[]
for i in range(n):
    elemnt=int(input())
    a.append(elemnt)
print(a)
print("the multiplication of all the elements of list is",mul(a))
