def factorial(n):
    facto=1
    for i in range(1,n+1):
        facto=facto*i
    return(facto)
a=int(input("enter the number whose factorial is to be calculated:"))
fact=factorial(a)
print("factorial of given number is",fact)
