import turtle

# Colored Circle (Denys fisher spirograph)
turtle.pensize(5)
for _ in range(4):
  for color in ["red", "green", "blue"]:
    turtle.pencolor(color)
    turtle.circle(100)
    turtle.right(30)
turtle.done()
