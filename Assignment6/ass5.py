n=int(input("Enter any Number:"))

lst=[]
print("A List of Sqaure of First",n,"Prime Number is:")
for i in range(1,n+1):
    lst.append(i*i)
    
print(lst)