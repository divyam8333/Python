#Creating an Empty Set
s=set([])

n=int(input("Enter any Number:"))
N=n

x=2
while N!=0:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        s.add(x)
        N-=1
    x+=1

print("A set of First",n,"Prime Number is",s)