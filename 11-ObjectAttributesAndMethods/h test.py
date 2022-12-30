import turtle

def draw_letter(letter, size):
  # Draw the outline of the given letter using a series of
  # forward and backward moves and left and right turns.
  if letter.upper() == 'H':
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(180)
    turtle.forward(size / 2)
    turtle.left(90)

# Set the turtle's pen size and color
turtle.pensize(5)
turtle.pencolor('red')

# Move the turtle to the starting position for the letter
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

# Draw the letter "H"
draw_letter('H', 100)

# Hide the turtle and wait for the user to close the window
turtle.hideturtle()
turtle.exitonclick()
