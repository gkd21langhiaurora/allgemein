from gturtle import *

makeTurtle()

setPenColor("orange")
forward(100)
right(90)

setPenColor("blue")
setPenWidth(5)
forward(100)
left(90)

setPenColor("green")
setPenWidth(1)
back(100)

setPenColor("black")
left(90)
repeat 10:
    forward(5)
    penUp()
    forward(5)
    penDown()

right(90)