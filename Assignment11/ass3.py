def Prime(n):
   x=2
   while n!=0:
     for i in range(2,x):
       if x%i==0:
         break
     else:
       print(x,end=" ")
       n-=1
    
     x+=1

n=int(input("Enter any Number:"))
print("First",n,"Prime Numbers are:",end=" ")
Prime(n)

