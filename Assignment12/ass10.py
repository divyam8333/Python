def Cube(n):
    if n>0:
        print(n*n*n,end=" ")
        Cube(n-1)

N=int(input("Enter any Number:"))
Cube(N)