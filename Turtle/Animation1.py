import turtle

s=turtle.getscreen()
t1=turtle.Turtle()

s.bgcolor("black")
t1.width(2)
t1.speed(10)

col=('white','pink','cyan')
for i in range(300):
    t1.pencolor(col[i%3])
    t1.forward(i*4)
    t1.right(121)
