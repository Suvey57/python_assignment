def add(b):
    sum=0
    for i in range(len(b)):
        sum=sum+b[i]
    return(sum)

n=int(input("enter numbers of elements to be inputted in the list:"))
a=[]
for i in range(n):
    elemnt=int(input())
    a.append(elemnt)
print(a)
print("sum of all the elements of list is",add(a))
