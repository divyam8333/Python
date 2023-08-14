n=int(input("Enter any number:"))

i=2
print("All Prime factors of",n,"are",end=" ")
while n!=1:
    if n%i==0:
        print(i,end=" ")
        n=n/i
    else:
        i+=1
