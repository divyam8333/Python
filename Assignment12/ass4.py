def Even(n):
    if n!=0:
      print(2*n,end=" ")
      Even(n-1)


N=int(input("Enter any Number:"))
Even(N)