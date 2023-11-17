import turtle
win = turtle.Screen()
win.bgcolor('black')

t = turtle.Turtle()
t.color('red')

for i in range(36):
    t.forward(10 + i * 5)
    t.left(90)
    t.forward(10 + i * 5)
    t.left(90)
    t.forward(10 + i * 5)
    t.left(90)
    t.forward(10 + i * 5)
    t.left(80)
turtle.exitonclick()