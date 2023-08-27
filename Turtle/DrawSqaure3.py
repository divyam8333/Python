import turtle 

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t1.pencolor("black")
t1.fillcolor("lightblue")
t1.shape("square")
t1.shapesize(5,5,3)

t1.penup()
t1.goto(200,200)
t1.stamp()

t1.penup()
t1.goto(-200,200)
t1.stamp()

t1.penup()
t1.goto(-200,-200)
t1.stamp()

t1.penup()
t1.goto(200,-200)
t1.stamp()
