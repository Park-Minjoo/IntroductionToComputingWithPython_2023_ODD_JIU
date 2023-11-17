import turtle
win = turtle.Screen()
win.bgcolor('black')

one = turtle.Turtle()
one.color('red')
one.pensize(3)
def n_one(n, size):
    for i in range(n):
        one.circle(size)
        one.left(360.0/n)
n_one(20, 70)
turtle.exitonclick()