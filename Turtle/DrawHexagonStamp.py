import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()

i=0
while i<10:
    t1.forward(100)
    t1.left(60)
    t1.stamp()
    i+=1

t1.ht()
