from gturtle import *

makeTurtle()
hideTurtle()

# Startpunkt unten links im Haus, dann im Gegenuhrzeigersinn einmal das Quadrat machen
right(90)
repeat 4:
    forward(185)
    left(90)

# Diagonale von unten links nach oben rechts, Dreieck oberhalb, Diagonale von oben rechts nach unten links
# Länge der Diagonale: d = sqrt(2) * s
left(45)
forward(sqrt(2) * 185)

repeat 2:
    left(90)
    forward(sqrt(2) * 185 / 2)

left(90)
forward(sqrt(2) * 185)
