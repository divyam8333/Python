print("Armstrong Number Under 1000 are:")

for i in range(1,1000):
    n=i
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+(rem*rem*rem)
        n=n//10

    if sum==i:
        print(i)
 
 