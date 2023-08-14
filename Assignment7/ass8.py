str=input("Enter any String:")

s1=""
i=0
for x in str:
    if str.index(x)==i:
        s1=s1+x
    i+=1

print(s1)