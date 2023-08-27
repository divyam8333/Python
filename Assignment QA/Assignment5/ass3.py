n=int(input("Enter any Number:"))
sum=0
N=n

while(N):
    rem=N%10
    sum=sum+(rem*rem*rem)
    N=N//10

if sum==n:
    print(n,"is a Armstrong Number")
else:
    print(n,"is not a Armstrong Number")