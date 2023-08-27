str1=input("Enter any String:")
                                     # -1         -1
str2=str1[-1::-1]              #slice(start,end,stop)

if str1==str2:
    print(str1,"is a Palindrome")
else:
    print(str1,"is not a Palindrome")