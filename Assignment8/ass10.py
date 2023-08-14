print("Enter Elements Seprated by Comma for a tuple:")
t=tuple([eval(i) for i in input().split(',')])

print("Greatest Number in a given tuple is:",max(t))
print("Smallest Number in a given tuple is:",min(t))