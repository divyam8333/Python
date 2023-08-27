#Creating an Empty List
lst=[]

n=int(input("Enter number of elements:"))
print("Enter any",n,"Strings:")
for i in range(0,n):
    str=input()
    lst.append(str)

lst.sort()
print(lst)