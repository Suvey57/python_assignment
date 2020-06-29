a=input("enter a string:")
b="ing"
if len(a)>=3:
    if a[-3::]!=b:
        a=a+'ing'
    else:
        a=a+'ly'
print(a)


    
