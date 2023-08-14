n=int(input("Enter any Number:"))
i=2
x=0                  #We have to exclude 1 and the no. itself
while i<n:
    if n%i==0:
        x=1
        break
    i+=1

if x==1:
    print(n,"is not a Prime Number")
else:
    print(n,"is a Prime Number")

