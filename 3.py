a=input("enter a string:")
c=list(a)
for i in range(1,len(a),1):
    if c[i].lower()==c[0].lower():
        c[i]="$"
d= ''.join(c)
print(d)


