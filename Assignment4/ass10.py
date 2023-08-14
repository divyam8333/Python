print("Enter any 2 Numbers:")
a=int(input())
b=int(input())

H=a if a<b else b
while H<=1:
    if a%H==0 and b%H==0:
        break
    H-=1

print("H.C.F of",a,"and",b,"is",H)