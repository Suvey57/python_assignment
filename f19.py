from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
n=int(input("enter a number upto which fibonacci is to be found:"))

print("Fibonacci series upto n:")

print(fib_series(n))