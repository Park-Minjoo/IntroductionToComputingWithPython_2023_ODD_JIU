import turtle
t = turtle.Turtle()
t.color("blue")

for i in range(36):
    t.left(10)
    for j in range(4):
        t.forward(100)
        t.left(90)
turtle.exitonclick()