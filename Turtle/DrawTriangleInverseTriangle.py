import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t1.pencolor("black")
t1.penup()
t1.goto(-200,-50)
t1.pendown()

t1.fillcolor("lightblue")
t1.begin_fill()

t1.left(60)
t1.fd(400)
t1.right(120)
t1.fd(400)
t1.right(120)
t1.fd(400)               #t1.goto(-200,-50) 

t1.penup()
t1.goto(200,180)
t1.pendown()
t1.fd(400)
t1.left(120)
t1.fd(400)
t1.left(120)
t1.fd(400)

t1.end_fill()
t1.ht()