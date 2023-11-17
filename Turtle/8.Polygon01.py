import turtle

wn = turtle.Screen()
wn.bgcolor("lightpink")
wn.title("Draw Polygon")

a = turtle.Turtle()
a.color("grey")
a.pensize(5)

a.penup()
a.goto(150, 150)
a.pendown()

for i in range(4):
    a.forward(120)
    a.left(90)
turtle.exitonclick()
