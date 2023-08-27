import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t1.penup()
t1.goto(200,200)
t1.pendown()
t1.fillcolor("lightblue")

t1.begin_fill()
t1.goto(-200,200)
t1.goto(-200,-200)
t1.goto(200,-200)
t1.goto(200,200)
t1.end_fill()

#draw small circle
l=[(150,150,"red"),(-25,150,"green"),(-25,-25,"brown"),(150,-25,"yellow")]
for xyc in l:
     x,y,c=xyc
     t1.penup()
     t1.goto(x,y)
     t1.pendown()
     t1.fillcolor(c)
     t1.begin_fill()
     t1.goto(x-125,y)
     t1.goto(x-125,y-125)
     t1.goto(x,y-125)
     t1.goto(x,y)
     t1.end_fill()

t1.ht()
