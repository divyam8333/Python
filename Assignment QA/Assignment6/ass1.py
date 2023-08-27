lst=[]       #Creating an Empty List

n=int(input("Enter Number of Elements:"))
print("Enter any",n,"Numbers:")
for i in range(0,n):
    num=int(input())
    lst.append(num)            #Adding Elements in list 

lst.sort()
print(lst)