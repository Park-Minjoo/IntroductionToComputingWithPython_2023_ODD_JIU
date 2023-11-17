import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")

a = turtle.Turtle()
a.color("black")
a.pensize(7)

for i in range(20, 110, 20):
    a.penup()
    a.goto(i, i)
    a.pendown()
    for j in range(3):
        a.forward(120)
        a.left(120)
turtle.exitonclick()
