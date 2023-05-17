# import turtle and the screen
import turtle
from turtle import Turtle, Screen

# turtle is built on tkinter so we can use tkinter for our buttons
from tkinter import *

# initialize pointer

pointer = Turtle('turtle')


# while dragging pointer, set direction towards drag and move pointer
def dragging(x, y):
    pointer.ondrag(None)
    pointer.setheading(pointer.towards(x, y))
    pointer.goto(x, y)
    pointer.ondrag(dragging)


# change color of drawing
def changeColor(color):
    pointer.color(color)


# change pen size, if it gets too small, stop decreasing and vice versa
def changePenSize(size):
    curr = pointer.pensize()
    newSize = curr + size
    if newSize < 1:
        newSize = 1
    elif newSize > 50:
        newSize = 50
    pointer.pensize(newSize)

# move pointer to mouse pos
def moveTurtle(x, y):
    pointer.penup()
    pointer.goto(x, y)
    pointer.pendown()


screen = Screen()

canvas = screen.getcanvas()

# set buttons for color
# lambda is used so we can refer to the function instead of running the function and getting a return value
redButton = Button(canvas.master, text="Red", command=lambda: changeColor("red"))
redButton.pack()
redButton.place(x=30, y=30)

blackButton = Button(canvas.master, text="Black", command=lambda: changeColor("black"))
blackButton.pack()
blackButton.place(x=70, y=30)

greenButton = Button(canvas.master, text="Green", command=lambda: changeColor("green"))
greenButton.pack()
greenButton.place(x=120, y=30)

blueButton = Button(canvas.master, text="Blue", command=lambda: changeColor("blue"))
blueButton.pack()
blueButton.place(x=170, y=30)

# set buttons for thickness of pointer
thicknessButton = Button(canvas.master, text='Pen Size')
thicknessButton.pack()
thicknessButton.place(x=650, y=30)

thicknessUp = Button(canvas.master, text='+', command=lambda: changePenSize(2))
thicknessUp.pack()
thicknessUp.place(x=700, y=30)

thicknessDown = Button(canvas.master, text='-', command=lambda: changePenSize(-2))
thicknessDown.pack()
thicknessDown.place(x=635, y=30)

pointer.speed('fastest')

pointer.ondrag(dragging)

turtle.onscreenclick(moveTurtle)

screen.mainloop()
