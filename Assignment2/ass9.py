a=int(input("Enter real part:"))
b=int(input("Enter Imaginary part:"))

c=complex(a,b)
print(c)

real_part=c.real
imaginary_part=c.imag

if real_part>imaginary_part:
   print("Greater no. is Real Part")
else:
   print("Greater no. is Imaginary Part")