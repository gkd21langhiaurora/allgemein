from gturtle import *

makeTurtle()
left(30)
repeat 4:
    repeat 60:
        forward(3)
        right(1)
    right(120)
    repeat 60:
        forward(3)
        right(1)
    right(120)
    right(360 / 4)
right(30)