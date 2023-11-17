import turtle
def hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)

turtle.color('red')
hexagon()

for i in range(6):
    hexagon()
    turtle.forward(100)
    turtle.right(60)
turtle.exitonclick()