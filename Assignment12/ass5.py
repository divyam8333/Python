def Odd(n):
    if n>0:     #Base Case
        Odd(n-1)     #Recursive Case
        print(2*n-1,end=" ")

N=int(input("Enter any Number:"))
Odd(N)
        