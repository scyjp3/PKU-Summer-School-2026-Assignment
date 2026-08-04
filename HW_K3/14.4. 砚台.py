import turtle

t = turtle.Turtle()
t.speed(2)


t.color("black")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

t.penup()
t.forward(180)
t.left(90)
t.forward(100)
t.pendown()
t.color("gray")
t.begin_fill()
t.circle(80)
t.end_fill()

turtle.done()
