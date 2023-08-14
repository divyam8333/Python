eng=int(input("Enter English Marks:"))
math=int(input("Enter Mathematics Marks:"))
hindi=int(input("Enter Hindi Marks:"))
phy=int(input("Enter Physics Marks:"))
chem=int(input("Enter Chemistry Marks:"))

avg=(eng+math+phy+hindi+chem)/5

if eng<=100 and hindi<=100 and math<=100 and phy<=100 and chem<=100:
    if avg>=33:
         print("** ------------------**")
         print("Result: PASS")
         print("------------------")
         print("Percentage:",avg)
         print("------------------")
         if avg>=60:      
          print("First Division")
         elif avg>=45:    
            print("Second Division")
         elif avg>=33:
            print("Third Division")
         print("------------------")
else:
    print("Chutiye Aukat ke hisab se no. daal")