lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    elemnt = int(input()) 
    lst.append(elemnt)
print(lst)
c=max(lst)
print(c)