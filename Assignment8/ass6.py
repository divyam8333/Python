t=()
l=[]

print("Enter any 5 Numbers:")
for i in range(5):
    x=int(input())
    l.append(x)

#Type Casting
t=tuple(l)

sum=0
for i in t:
    sum=sum+i

print("Sum of the Elements of the Tuple:",sum)