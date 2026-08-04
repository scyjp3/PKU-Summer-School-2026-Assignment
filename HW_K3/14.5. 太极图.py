import turtle

t = turtle.Turtle()
t.speed(2)
t.pensize(3)

t.color("white")
t.begin_fill()
t.circle(50, 180)
t.end_fill()

t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(50, 180)
t.end_fill()

t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.left(90)
t.forward(60)
t.left(90)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(100,180)
t.end_fill()

t.circle(100,180)



turtle.done()
