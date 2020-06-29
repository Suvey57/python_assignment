def reversed(name,length):
    reverse=""
    while(length>0):
        reverse+=name[length-1]
        length-=1
    return(reverse)

a=input("enter string to be reversed:")
lengt=len(a)
reversed_string=reversed(a,lengt)
print(reversed_string)