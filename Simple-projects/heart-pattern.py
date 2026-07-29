import turtle
import math
import random
import time

# ---------------- Text ----------------
screen = turtle.Screen()
screen.bgcolor("black")

writer = turtle.Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()

text = "Heart Design"

for i in range(len(text) + 1):
    writer.clear()
    writer.goto(0, 250)
    writer.write(
        text[:i],
        align="center",
        font=("Arial", 28, "bold")
    )
    time.sleep(0.1)

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Colorful Heart Animation")

# ---------------- Turtle ----------------
t = turtle.Turtle()
t.speed(10)
screen.tracer(3)          # Animation speed (1-10)
t.hideturtle()
t.pensize(2)

colors = [
    "red"
]

scale = 15          # Heart size

# ---------------- Draw Heart ----------------
for i in range(120):

    angle = (2 * math.pi * i) / 120

    x = 16 * (math.sin(angle) ** 3) * scale

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * scale

    t.penup()
    t.goto(0, 0)           # Start from the center
    t.pendown()

    t.color(random.choice(colors))
    t.goto(x, y)

    # Decorative star
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()