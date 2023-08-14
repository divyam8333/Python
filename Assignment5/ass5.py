start=int(input("Enter Starting boundary Value:"))
end=int(input("Enter Ending Boundary Value:"))

step=int(input("Enter Step's Size:"))

print("Sequence of Numbers with",step,"step size is:")
for i in range(start,end+1,step):
    print(i,end=" ")
