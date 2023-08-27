print("Enter 2 Numbers:")
a=int(input())
b=int(input())

for i in range(1,a*b):
    if i%a==0 and i%b==0:
        break

print("L.C.M of",a,"and",b,"is",i)