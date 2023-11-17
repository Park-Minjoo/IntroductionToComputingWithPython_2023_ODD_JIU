import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Draw Triangle")

t = turtle.Turtle()
t.color("hotpink")
t.pensize(3)

t.penup()
t.goto(0, 250)
t.pendown()

for i in range(3):
    t.forward(80)
    t.left(120)

t.penup()
t.right(180)
t.forward(80)
turtle.exitonclick()
