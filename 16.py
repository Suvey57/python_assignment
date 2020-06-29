lst = [] 
sum=0
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    elemnt = int(input()) 
    lst.append(elemnt)
    sum=sum+lst[i]
print(lst)
print(sum)