n1=int(input("Enter Starting Range:"))
n2=int(input("Enter Ending Range:"))

print("Squares of Numbers from",n1,"and",n2)
for i in range(n1,n2+1):
    print(i*i,end=" ")