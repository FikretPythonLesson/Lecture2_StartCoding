import turtle

# Drawing a dashed line 
# ----------------------
length = 15

for i in range(1,10):
    turtle.forward(length)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
    
turtle.done()

