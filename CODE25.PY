#WAPP to Implement Concentric Circles Using Turtle Graphics

import turtle

screen = turtle.Screen()
screen.title("Concentric Circles")

pen = turtle.Turtle()
pen.speed(3)

radii = [40, 80, 120, 160, 200]

for radius in radii:
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)

pen.hideturtle()
turtle.done()
