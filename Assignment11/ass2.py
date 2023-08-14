def RevBinary(n):
    i=1
    binary=0
    while n!=0:
      rem=n%2
      binary=binary+(i*rem)
      i=i*10
      n=n//2
    
    return binary

N=int(input("Enter any Number:"))

rev=str(RevBinary(N))[::-1]
print("Reverse of Binary Representation of",N,"is",rev)

def Prime(n):
    i=2
    while i<=n:
      x=0
      for j in range(2,i):
         if n%j==0:
          x=1
          break
    
      if x==0:
        print(n)
        i+=1
    

n=int(input("Enter any Number:"))
print("First",n,"Prime Number is",Prime(n))
