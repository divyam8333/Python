print("Enter Elements seprated by comma for Tuple:")
t=tuple([eval(i) for i in input().split(',')])


x=int(input("Enter that number which you want to check frequency in a tuple:"))
print("The Frequency of",x,"in a given tuple is",t.count(x))