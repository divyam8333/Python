print("Enter any 3 Names:")
a=input()
b=input()
c=input()

if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<c<a:
    print(b,c,a)
elif c<b<a:
    print(c,b,a)
elif  b<a<c:
    print(b,a,c)
else:
    print(c,a,b)


