from re import I


n=int(input("Enter any Number:"))

i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1

print("Factorial of",n,"is",fact)