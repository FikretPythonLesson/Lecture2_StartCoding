import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.penup()

for _ in range(12):
    turtle.shape("turtle")
    turtle.forward(100)
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    
    turtle.back(10)
    turtle.shape("classic")
    turtle.pendown()
    turtle.back(10)
    turtle.penup()
    turtle.back(80)
    turtle.left(360/12)
    
turtle.shape("turtle")
turtle.stamp()

turtle.done()
