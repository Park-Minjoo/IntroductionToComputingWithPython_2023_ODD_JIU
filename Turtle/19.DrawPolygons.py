import turtle
t=turtle.Turtle()
def drawPolygon(sideLength, numSides, color):
    t.color(color)
    turnAngle= 360 / numSides
    for i in range(numSides):
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)
for i in range(3):
    t.penup()
    t.setposition(40*i, 0)
    drawPolygon(20, 6, "blue")
for i in range(5):
    t.penup()
    t.setposition(40*(i-2), -100)
    drawPolygon(40, 4, "violet")
turtle.exitonclick()