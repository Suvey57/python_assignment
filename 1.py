a=input("enter a string:")
count = {}
for s in a:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
    print (key, count[key])
    


