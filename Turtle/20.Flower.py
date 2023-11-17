import turtle
def flower(t, n, r, angle):
    for i in range(n):
        for i in range(2):
            t.circle(r,angle)
            t.left(180-angle)
        t.left(360/n)
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
b = turtle.Pen()
b.color("violet")
move(b, -100)

for i in range(3):
    flower(b, 6, 30+(10*i), 60.0)
    b.width(2*i)
turtle.exitonclick()