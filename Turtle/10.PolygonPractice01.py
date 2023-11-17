import turtle

wn = turtle.Screen()
wn.bgcolor("lightpink")

a = turtle.Turtle()
a.color("grey")
a.pensize(5)

for i in range(20, 110, 20):
    a.penup()
    a.goto(i, i)
    a.pendown()
    for j in range(4):
        a.forward(120)
        a.left(90)
turtle.exitonclick()
