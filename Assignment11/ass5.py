def SumEven(l):
    even=0
    for i in l:
       if i%2==0:
          even=even+i
    return even

def SumOdd(l):  
    odd=0
    for i in l:
       if i%2!=0:
          odd=odd+i       
    return odd

l=[]
n1=int(input("How many Elements you want to insert:"))

print("Enter any",n1,"Numbers:")
for i in range(n1):
    n2=int(input())
    l.append(n2)

print("Sum of all Even numbers from a given list is",SumEven(l))
print("Sum of all Odd numbers from a given list is",SumOdd(l))
