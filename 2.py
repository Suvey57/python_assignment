a=input("enter a string:")
b=len(a)
if b>2:
        c=a[0]+a[1]+a[-2]+a[-1]
        print(c)
elif b==2:
    c=a*2
    print(c)
else:
    c=""
    print(c)
