num=int(input("Enter any number:"))

lst=[]
n=num
x=2
while n!=0:
    for i in range(2,x):
       if x%i==0:
         break
    else:
        lst.append(x)
        n-=1
        
    x+=1

print("A list of first",num,"Prime Number is:",lst)

