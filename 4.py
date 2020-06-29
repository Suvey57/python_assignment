a=input("enter first string:")
b=input("enter second string:")
c=list(a)
d=list(b)
for i in range(2):
    c[i]=b[i]
    d[i]=a[i]
e=''.join(c)
f=''.join(d)
g=e+' '+f
print(g)