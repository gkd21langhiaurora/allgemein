from gturtle import *

def quadrat(seite, richtung):
    repeat 4:
        forward(seite)
        # ___________________________
        right(90*richtung)
        
def reihe(anzahl_horizontal, seite, richtung):
    repeat anzahl_horizontal:
        quadrat(seite,richtung)
        
        # ___________________________
        penUp()
        right(90*richtung)
        forward(seite)
        right(-90*richtung)
        penDown()

def gitter(anzahl_vertikal, anzahl_horizontal, seite):
    richtung = 1
    repeat anzahl_vertikal:
        reihe(anzahl_horizontal, seite, richtung)
        
        # ___________________________
        penUp()
        backward(seite)
        penDown()
        
        # ___________________________
        richtung *= -1

makeTurtle()
hideTurtle()
gitter(3,5,20)

