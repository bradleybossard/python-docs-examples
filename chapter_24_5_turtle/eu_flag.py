import turtle
aze = turtle.Turtle()
aze.speed(0)
aze.shape('turtle')

def makeStar():
  heading_before_star = aze.heading()
  aze.setheading(0)
  for k in range(5):
    aze.forward(20)
    aze.right(144)
  aze.setheading(heading_before_star)

aze.setheading(-15)
for i in range(12):
  makeStar()
  aze.left(30)
  aze.penup()
  aze.forward(50)
  aze.pendown()

turtle.mainloop()
