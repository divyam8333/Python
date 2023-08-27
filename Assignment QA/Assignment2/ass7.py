import cmath

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

#Calculate the Discriminant
d=(b**2)-4*a*c

#Find 2 Solutions
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)

print("The Solutions are:",sol1,"and",sol2)