n=int(input("Enter any number:"))

print("Next Prime Number is",end=" ")
while True:
    n+=1
    x=0
    for i in range(2,n):
        if n%i==0:
            x=1
            break
    if x==0:
        print(n)
        break
    