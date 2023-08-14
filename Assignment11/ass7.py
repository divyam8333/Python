def Fibonacci(n):
    a,b=-1,1
    for i in range(n):
       c=a+b
       a=b
       b=c

    return c
     
n=int(input("Enter any Number:"))
print(n,"th term of Fibonacci Series is:",Fibonacci(n))
