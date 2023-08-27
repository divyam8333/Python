import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
s.title("Turtle Moves Like a Fan")
t1.pencolor("red")
t1.shape("turtle")
t1.shapesize(10,15,5)
for angle in range(0,901,90):
    t1.left(angle)
