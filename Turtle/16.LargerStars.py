import turtle
star = turtle.Turtle()
star.color('red')

for i in range(20):
    star.forward(i*50)
    star.right(144)
turtle.done()
turtle.exitonclick()