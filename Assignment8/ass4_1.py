t=()
l=[]


print("Enter any 5 Elements:")
for i in range(5):
    x=input()
    l.append(x)

l.reverse()

#typeCasting
t=tuple(l)   
print(t)