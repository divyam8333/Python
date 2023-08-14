lst=[]      #Creating an Empty List

n=int(input("Enter no. of Elements:"))
print("Enter any",n,"Elements:")
for i in range(0,n):
    num=int(input())
    lst.append(num)

lst.sort()
print("Largest Number is:",lst[-1])