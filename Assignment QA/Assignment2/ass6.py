#import calendar
#num=int(input("Enter any Month Number:"))
#res=calendar.month_name[num]
#print("Month Name is:" +str(res))

month=int(input("Enter any Month in Numeric format:"))

if month==1:
   print("31")
elif month==2:
   print("28/29")
elif month==3:
   print("31")
elif month==4:
   print("30")
elif month==5:
   print("31")
elif month==6:
   print("30")
elif month==7:
   print("31")
elif month==8:
   print("30")
elif month==9:
   print("31")
elif month==10:
   print("30")
elif month==11:
   print("31")
elif month==12:
   print("30")
else:
   print("Please enter valid month no.")