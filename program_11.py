import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Pattern Generator")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("cyan")

# Draw geometric pattern
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

# Draw spiral
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("yellow")

for i in range(100):
    t.forward(i * 2)
    t.right(91)

# Finish
turtle.done()