def Even(n):
    if n!=0:
      Even(n-1)
      print(2*n,end=" ")


N=int(input("Enter any Number:"))
Even(N)
