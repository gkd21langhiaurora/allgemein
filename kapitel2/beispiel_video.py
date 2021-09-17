from gturtle import *

# Eigenen Funktionen, Befehle
def quadrat100():
    repeat 4:
        forward(100)
        right(90)

def dreieck30():
    repeat 3:
        forward(30)
        right(120)

# Start des eigentlichen Programmes
makeTurtle()
hideTurtle()

repeat 8:
    # Zeichne ein Quadrat mit Seitenlänge 100
    quadrat100()
    
    
    # Zwischenschritt ist immer gleich
    left(45)
    # Farbe ändern...

penUp()
forward(200)
penDown()
# Zeichne ein Dreieck

dreieck30()

# Zeichne ein Quadrat mit Seitenlänge 100
quadrat100()