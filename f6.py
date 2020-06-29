def range(x,start,end):
    if (x<start or x>end):
        x=0
        return(x)
    else:
        x=1
        return(x)




i=int(input("enter initial range separated by sapce:"))
f=int(input("enter final range separated by sapce:"))
n=int(input("enter number:"))
c=range(n,i,f)
if c==0:
    print("the inputted number lies outside range")
else:
    print("the inputted number lies inside range")