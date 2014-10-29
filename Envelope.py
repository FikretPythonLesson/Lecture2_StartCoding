import turtle
import math

## Draw an envelope
# -----------------
turtle.shape("turtle")
turtle.pensize(4)
turtle.bgcolor("yellow")

turtle.color("blue", "red")
turtle.begin_fill()

kenar = 100
kosegen = math.sqrt(kenar**2 + kenar**2)
ucgenkenar  = kenar / math.sqrt(2)

turtle.forward(kenar)
turtle.left(90)
turtle.forward(kenar)
turtle.left(90)
turtle.forward(kenar)
turtle.left(90)
turtle.forward(kenar)
turtle.left(90)

turtle.left(45)
turtle.forward(kosegen)
turtle.left(90 + 45)
turtle.penup()
turtle.forward(kenar)
turtle.pendown()
turtle.left(90 + 45)
turtle.forward(kosegen)

turtle.left(90 + 45)
turtle.penup()
turtle.forward(kenar)
turtle.pendown()
turtle.left(45)
turtle.forward(ucgenkenar)
turtle.left(90)
turtle.forward(ucgenkenar)

turtle.end_fill()
turtle.done()
