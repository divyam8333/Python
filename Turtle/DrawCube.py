import turtle

s=turtle.getscreen()
t1=turtle.Turtle()
t1.pencolor("black")
t1.pensize(5)

#Draw a Rectangle
t1.fd(200)
t1.left(90)
t1.fd(200)
t1.left(90)
t1.fd(400)
t1.left(90)
t1.fd(200)
t1.lt(90)
t1.fd(200)

t1.penup()
t1.goto(100,-100)
t1.pendown()

#Draw a Rectangle
t1.fd(200)
t1.left(90)
t1.fd(200)
t1.left(90)
t1.fd(400)
t1.left(90)
t1.fd(200)
t1.lt(90)
t1.fd(200)

t1.penup()
t1.goto(300,100)
t1.pendown()
t1.goto(200,200)

t1.penup()
t1.goto(-200,200)
t1.pendown()
t1.goto(-100,100)

t1.penup()
t1.goto(-200,0)
t1.pendown()
t1.goto(-100,-100)

t1.penup()
t1.goto(200,0)
t1.pendown()
t1.goto(300,-100)