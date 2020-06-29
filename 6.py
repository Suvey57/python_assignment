a=input("enter a string:")
b=a.find('not')
c=a.find('poor')
if c>b:
    if (b==0 and a[:3:]=="not")or b>0:
      a= a.replace(a[b:(c+4)], 'good')
print(a)
