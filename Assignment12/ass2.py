def natural(n):
    if n!=0:
        natural(n-1)
        print(n,end=" ")


N=int(input("Enter any Number:"))
natural(N)
