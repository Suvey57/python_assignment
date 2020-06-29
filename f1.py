def max(a,b,c):
    if (a>b and a>c):
        return a
    if (b>c and b>a):
        return b
    else:
        return c
x=int(input("enter first number::"))
y=int(input("enter second number::"))
z=int(input("enter third number::"))
maximum=max(x,y,z)
print("the maximum of three numbers is",maximum)
    