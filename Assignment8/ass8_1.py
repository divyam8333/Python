t1=()
t2=()

l1=[]
l2=[]
print("Enter any 5 Elements for 1st Tuple:")
for i in range(5):
    x=input()
    l1.append(x)

print("Enter any 5 Elements for 2nd Tuple:")
for i in range(5):
    x=input()
    l2.append(x)

t1=tuple(l1)
t2=tuple(l2)

if t1==t2:
    print("Both Tuples are Same")
else:
    print("No,Tuples are not Same")