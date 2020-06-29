# a=input("enter a string:")
# for i in range(0,len(a),2):
#     print(a[i],end='')
a=input("enter a string")
b=""
for i in range(len(a)):
    if i%2==0:
        b=b+a[i]
print(b)
