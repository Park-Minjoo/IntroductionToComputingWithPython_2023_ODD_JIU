import turtle

t1 = turtle.Turtle()

for i in range(30, 500, 20):
    t1.forward(i)
    t1.left(60)

turtle.done
turtle.exitonclick()
