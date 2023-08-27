import turtle

s=turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()

i=0
while i<10:
    x=t1.stamp()     #Stamp() returns uniqe id
    t1.forward(100)
    t1.left(60)
    t1.clearstamp(x)  #ClearStamp() delete the stamped turtle
    i+=1

t1.ht()