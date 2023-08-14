print("Enter any three number:")
a=int(input())
b=int(input())
c=int(input())

if a>b:
    if a>c:
        print(a,"is a Largest Number")
    else:
        print(c,"is a Largest Number")
else:
    if b>c:
        print(b,"is a Largest Number")
    else:
        print(c,"is a Largest Number")