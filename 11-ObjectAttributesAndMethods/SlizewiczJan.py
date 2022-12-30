import turtle


turtle.setup(400, 400)
turtle.bgcolor("black")


def draw_star(x, y, size, color):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)

def draw_triangle(x, y, size, color):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)

def draw_circle(x, y, size, color):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.circle(size)

def draw_rectangle(x, y, width, height, color):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)

def draw_square(x, y, size, color):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)


for i in range(4):
  # draw_star(-100, 100, 50, "yellow")
  # draw_triangle(-50, 50, 50, "red")
  # draw_circle(0, 0, 50, "blue")
  # draw_rectangle(50, -50, 100, 50, "green")
  # draw_square(100, -120, 25, "purple")

  draw_star(0, 0, 50, "yellow")
  draw_triangle(0, -100, 50, "red")
  draw_circle(0, -50, 50, "blue")
  draw_rectangle(50, -50, 50, 25, "green")
  draw_square(-50, -50, 50, "purple")


turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
turtle.pencolor("white")
turtle.write("Jan Ślizewicz 226656 ZSIA1-1112", align="right", font=("Arial", 12, "normal"))


turtle.exitonclick()
