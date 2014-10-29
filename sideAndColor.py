import turtle

##sides = int(raw_input("Enter the number of sides: "))
##length = int(raw_input("Enter the length of each side: "))
##color = raw_input("Enter the fill color: ")

# or we can get all value in one line
sides, length, color = raw_input("Enter sides, length and color: ").split()
sides = int(sides)
length = int(length)

turtle.color(color)
turtle.begin_fill()

for _ in range(sides):
    turtle.forward(length)
    turtle.left(360/sides)

turtle.end_fill()
turtle.done()
