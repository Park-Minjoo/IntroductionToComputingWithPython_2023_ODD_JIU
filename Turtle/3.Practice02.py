import turtle
t1 = turtle.Turtle()

for i in range(30, 300, 20):
    t1.forward(i)
    t1.left(60)

turtle.exitonclick()