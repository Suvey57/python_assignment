
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = (input()) 
    lst.append(ele)     
print(lst) 

print(Remove(lst)) 
