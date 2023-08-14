n1=int(input("Enter Starting Range:"))
n2=int(input("Enter Ending Range:"))

print("All Prime Numbers b/w",n1,"and",n2,"is",end=" ")
for i in range(n1+1,n2):
    x=0
    for j in range(2,i):
        if i%j==0:
            x=1
            break
    if x==0:
        print(i,end=" ")