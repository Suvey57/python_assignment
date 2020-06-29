key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
a={0:2,1:3}
a.update({key:value})
print("Updated dictionary is:")
print(a)