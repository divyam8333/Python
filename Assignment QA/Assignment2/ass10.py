eng=int(input("Enter English's Marks:"))
hindi=int(input("Enter Hindi's Marks:"))
math=int(input("Enter Mathematics's Marks:"))
phy=int(input("Enter Physics's Marks:"))
che=int(input("Enter Chemistry's Marks:"))

avg=(eng+hindi+phy+math+che)/5
print("Percentage:",avg)

if avg>=60:
    print("Result: PASS")
    print("First Division")
elif avg>=45:
    print("Result: PASS")
    print("Second Division")
elif avg>=33:
    print("Result: PASS")
    print("Third Division")
else:
    print("Result: FAIL")

