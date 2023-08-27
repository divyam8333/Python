print("Enter Elements Seprated by comma for 1st Tuple:")
t1=tuple([eval(e) for e in input().split(',')])

print("Enter Elements Seprated by comma for 2nd Tuple:")
t2=tuple([eval(e) for e in input().split(',')])

if t1==t2:
    print("Both Tuples are Same")
else:
    print("No,Tuples are not Same")
