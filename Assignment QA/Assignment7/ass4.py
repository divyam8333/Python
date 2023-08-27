str=input("Enter any String:")
ch=input("Enter any Character:")

count=0
n=len(str)
for i in range(n):
    if str[i]==ch:
        count+=1

if count==0:
    print(ch,"not found in a",str)
else:
    print(ch,"occuerred",count,"times in",str)
