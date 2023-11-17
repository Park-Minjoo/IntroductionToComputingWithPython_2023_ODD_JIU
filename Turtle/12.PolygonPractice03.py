import turtle
t = turtle.Turtle()

def drawPolygon(sideLength, numSides, color):
    t.color(color)
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)
t.penup()
t.setposition(-50, 0)
drawPolygon(50, 5, 'blue')

t.penup()
t.setposition(100, 0)
drawPolygon(50, 8, 'hotpink')
turtle.exitonclick()
