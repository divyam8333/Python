def nextPrime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n

n=int(input("Enter any Number:"))
print("Next Prime Number is",nextPrime(n))

