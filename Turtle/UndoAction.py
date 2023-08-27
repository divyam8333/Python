import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.pencolor("red")
t2.pencolor("green")

t1.penup()
t2.penup()
t1.goto(-200,0)
t2.goto(200,0)
t2.left(180)
t1.pendown()
t2.pendown()

for i in range(1,11):
    t2.fd(35)
    t2.penup()
    t2.fd(5)
    t2.pendown()

for e in range(3):
   for i in range(1,11):
      t2.undo()
      t2.undo()
      t2.undo()
      t2.undo()
      t1.fd(35)
      t1.penup()
      t1.fd(5)
      t1.pendown()
   for i in range(1,11):
       t1.undo()
       t1.undo()
       t1.undo()
       t1.undo()
       t2.fd(35)
       t2.penup()
       t2.fd(5)
       t2.pendown()


    

    
