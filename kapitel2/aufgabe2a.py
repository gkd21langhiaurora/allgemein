from gturtle import *

# Eigene Befehle definieren

def blatt():
    
    repeat 2:
        repeat 120:
            forward(3)
            right(1)
        right(60)

# Startpunkt des Programmes
makeTurtle()
hideTurtle()

left(60)

repeat 12:
    blatt()
    left(360 / 12)

right(60)