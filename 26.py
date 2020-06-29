a=input("enter string to be inputted before the elements of list:")
n=int(input("enter number of elements to be inputted in a list:"))
b=[]
for i in range(n):
    c=int(input())
    b.append(c)

print(b)
for i in range(n):
    b[i]=a+str(b[i])
print(b)