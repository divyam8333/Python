s1=set([])
s2=set([])

print("Enter any 5 Numbers for 1st Set:")
for i in range(5):
    x=int(input())
    s1.add(x)

print("Enter any 5 Numbers for 2nd Set:")
for i in range(5):
    x=int(input())
    s2.add(x)

s3=s1.union(s2)
print("Union of two sets is",s3)