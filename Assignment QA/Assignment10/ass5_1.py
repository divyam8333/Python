d={}
n=int(input("Enter No. of Key-Values Pair:"))

for i in range(n):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value:"))
    d.update({key:value})

sum=0
for i in d:
    sum=sum+d[i]

print("The Sum of Values is:",sum)
