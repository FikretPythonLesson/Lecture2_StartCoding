import turtle

# Drawing a dashed line (dashes become larger as line progress)
# --------------------------------------------------------------
length = 15
for i in range(1,10):
    turtle.forward(length + i)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
turtle.done()
