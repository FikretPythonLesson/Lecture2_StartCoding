import turtle

legs = int(raw_input(" Enter the number of legs: "))
for _ in range(1, legs + 1):
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.backward(100)
    turtle.left(360/legs)

turtle.done()
