#Creating an Empty List
lst=[]
sum=0

n=int(input("Enter no. of Elements:"))
print("Enter any",n,"Digits:")
for i in range(0,n):
    num=int(input())
    lst.append(num)

for i in lst:
    sum=sum+i

print("Sum of all the integers of the list:",sum)
