lst = [] 
mult=1
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    elemnt = int(input()) 
    lst.append(elemnt)
    mult=mult*lst[i]
print(lst)
print(mult)