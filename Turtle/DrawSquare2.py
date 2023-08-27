import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t1.penup()
t1.goto(50,50)
t1.pendown()

t1.begin_fill()
t1.pencolor("black")
t1.fillcolor("lightblue")
t1.goto(-50,50)
t1.goto(-50,-50)
t1.goto(50,-50)
t1.goto(50,50)
t1.ht()
t1.end_fill()
