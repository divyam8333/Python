def Odd(n):
    if n>0:     #Base Case
        print(2*n-1,end=" ")
        Odd(n-1)     #Recursive Case

N=int(input("Enter any Number:"))
Odd(N)
        