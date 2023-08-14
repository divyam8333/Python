def Cube(n):
    if n>0:
        Cube(n-1)
        print(n*n*n,end=" ")

N=int(input("Enter any Number:"))
Cube(N)