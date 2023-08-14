def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
        

N=int(input("Enter any Positive Number:"))
if N>0:
   print("Sum of First",N,"Natural Number is:",sum(N))