def prime_check(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        return("prime")
    else:
        return("not prime")

n = int(input("Enter the number\n"))
print(prime_check(n))
