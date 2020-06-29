def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  

dict = {'a': 100, 'b':200, 'c':300} 
key=input("enter key to be checked::")
checkKey(dict,key)
