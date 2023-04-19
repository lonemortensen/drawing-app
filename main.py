# =======================================================================
# Project: Drawing App
# Description: An interactive app built with Python.
# The app lets users:
# - select one of three geometric shapes for the app to draw.
# Background: Coursework for Skillcrush's "Getting Started with Python" course.

# ==== *** ====

# The main.py file contains code that:
# - uses the Turtle module to draw three different geometric shapes.
# - promts the user for input for which shape they want the app to draw.
# - uses for loops and the range() function to create the shapes.
# =======================================================================

import turtle as turtle
import random

print(
    "Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!"
)

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!",
             font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()


# Draws star:
def star():
    for i in range(0, 5):
        turtle.pensize(2)
        turtle.pencolor("blue")
        turtle.right(213)
        turtle.forward(110)


# Draws square:
def square():
    for i in range(0, 4):
        turtle.pensize(8)
        turtle.pencolor("red")
        turtle.right(90)
        turtle.forward(100)


# Draws hexagon:
def hexagon():
    for i in range(0, 6):
        turtle.pensize(4)
        turtle.pencolor("green")
        turtle.right(60)
        turtle.forward(100)


# Gets user input and calls the relevant function:
selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
    print("Excellent choice! Go to the result tab to see your creation.")
    star()
elif selection == "2":
    print("Excellent choice! Go to the result tab to see your creation.")
    square()
elif selection == "3":
    print("Excellent choice! Go to the result tab to see your creation.")
    hexagon()
