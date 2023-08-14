lst=[]
num=int(input("Enter No. of Elements in a List:"))

print("Enter any",num,"Numbers:")
for i in range(num):
    n=int(input())
    lst.append(n)

even=0
odd=0
for i in range(num):
    if lst[i]%2==0:
        even=even+lst[i]
    else:
        odd=odd+lst[i]

print("Sum of all Even no. is:",even)
print("Sum of all Odd No. is",odd)