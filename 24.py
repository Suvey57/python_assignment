def copyandcloning(cl): 
   copylist = cl[:] 
   return copylist 

A=list()
n1=int(input("Enter the size of the List ::"))
print("Enter the Element of List ::")
for i in range(int(n1)):
   k=int(input(""))
   A.append(k)
clon = copyandcloning(A) 
print("Original or Before Cloning The List Is:", A) 
print("After Cloning:", clon) 