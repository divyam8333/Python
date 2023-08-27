set1={1,2,3,5,7}
set2={1,2,3,5,7}

x=0
for  i in set1:
    for i in set2:
        if set1==set2:
            x+=1
            
if x==5:
    print("Both Set are same")
else:
   print("No,Sets are Not Same")