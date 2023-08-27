n=int(input("Enter any number: "))

print("First",n,"Even Natural numbers in reverse order are ",end=" ")
for i in range(n*2,1,-2):
  print(i,end=" ")