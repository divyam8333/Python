num1=int(input("Enter Starting Range:"))
num2=int(input("Enter Ending Range:"))

print("All Prime Numbers between",num1,"and",num2,":")
for i in range(num1,num2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
        