import turtle

n = int(input("请输入边长n（100-300）："))
if n < 100 or n > 300:
    print("边长必须在100-300之间")
else:
    t = turtle.Turtle()
    t.speed(2)

    t.color("red", "yellow")
    t.pensize(3)
    t.begin_fill()
    for _ in range(3):
        t.forward(n)
        t.left(120)
    t.end_fill()

    t.penup()
    t.goto(-n * 0.15, -n * 0.3)
    t.pendown()
    t.color("black")
    t.pensize(n * 0.08)
    t.forward(n * 0.3)

    t.penup()
    t.goto(-n * 0.15, -n * 0.5)
    t.dot(n * 0.12, "black")

    turtle.done()