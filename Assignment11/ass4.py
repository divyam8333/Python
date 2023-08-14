def lenStr(str):
    count=0
    for i in str:
       count+=1
    return count


str=input("Enter any String:")


print("Length of given string",str,"is:",lenStr(str))