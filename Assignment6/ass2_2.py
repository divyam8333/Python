lst=[]      #Creating an Empty List

n=int(input("Enter no. of Elements:"))
print("Enter any",n,"Elements:")
for i in range(0,n):
    num=int(input())
    lst.append(num)

print("Largest Number is:",max(lst))  #max(list_name)