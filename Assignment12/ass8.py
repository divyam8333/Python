def Square(n):
  if n>0:
    Square(n-1)
    print(n*n,end=" ")


N=int(input("Enter any Number:"))
Square(N)