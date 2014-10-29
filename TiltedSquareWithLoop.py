import turtle
# Tilted square with variable
# ---------------------------
# Change above program's angle and size values with variables
# Play with different angle and size values.

turtle.shape("turtle")
turtle.pensize(4)
turtle.bgcolor("yellow")

turtle.color("blue", "red")
turtle.begin_fill()

size = 300
angle = 10

for _ in range(3):
    turtle.left(angle)   # tilt with the given angle
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

turtle.end_fill()
turtle.done()
