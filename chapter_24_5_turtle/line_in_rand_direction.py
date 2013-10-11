import turtle
from random import randint

x = 50

turtle = turtle.Turtle()

degrees = randint(0, 360)
turtle.left(degrees)
turtle.forward(x)

turtle.getscreen()._root.mainloop()
