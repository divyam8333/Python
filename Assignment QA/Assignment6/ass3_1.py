lst=[]

n=int(input("How many Elements in list:"))
print("Enter any",n,"Numbers:")

for i in range(0,n):
    num=int(input())
    lst.append(num)
    

sum=0
for i in range(0,n):
    sum=sum+lst.pop()

print(sum)