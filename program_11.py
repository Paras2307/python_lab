import turtle

# Create screen
screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# User input
color = input("Enter pen color (red, blue, green, yellow): ")
size = int(input("Enter pattern size: "))

pen.color(color)

# Draw spiral pattern
for i in range(size):
    pen.forward(i * 2)
    pen.right(91)

# Draw a colorful geometric pattern
colors = ["red", "yellow", "blue", "green", "purple"]

pen.penup()
pen.goto(0, 0)
pen.pendown()

for i in range(100):
    pen.color(colors[i % len(colors)])
    pen.forward(100)
    pen.right(144)

# Finish drawing
pen.hideturtle()
turtle.done()