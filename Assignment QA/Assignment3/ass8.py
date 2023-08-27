n=int(input("Enter any Number:"))
i=1
sum=0

while i<=n*2:
    if i%2!=0:
        sum=sum+i
    i+=1

print("Sum of first",n,"Odd Natural Numbers are",sum)