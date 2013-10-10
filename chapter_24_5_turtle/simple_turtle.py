import turtle             # Allows us to use turtles

turtle = turtle.Turtle()    # Create a turtle, assign to alex

turtle.getscreen().setup(200, 200, 0, 0)
turtle.getscreen().bgcolor("orange")

turtle.forward(50)          # Tell alex to move forward by 50 units
turtle.left(90)             # Tell alex to turn by 90 degrees
turtle.forward(30)          # Complete the second side of a rectangle

turtle.getscreen()._root.mainloop()
