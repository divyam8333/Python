num=int(input("Enter any Number:"))
print("First",num,"Prime Numbers are:")

x=2
while num:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=" ")
        num-=1

    x+=1

