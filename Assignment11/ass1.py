def LCM(n1,n2):
    for i in range(1,n1*n2+1):
      if i%n1==0 and i%n2==0:
          break
    return i

print("Enter two numbers:")
n1=int(input())
n2=int(input())

print("L.C.M of",n1,"and",n2,"is",LCM(n1,n2))