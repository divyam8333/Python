from re import I


n=int(input("Enter any Number:"))

fact=1
i=1
while i<=n*2:
    if i%2!=0:
        fact=fact*i
    i+=1

print("Product of First",n,"Odd Natural Numbers are:",fact)
