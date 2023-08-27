n=int(input("Enter any number:"))

x=1
print("First ",n,"Prime Numbers are")
while n:
    y=0
    for i in range(2,x):
        if x%i==0:
            y=1
            break
    if y==0:
        print(x,end=" ")
        n-=1
    x+=1