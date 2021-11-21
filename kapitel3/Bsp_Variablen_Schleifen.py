from gturtle import *

def quadrat(seite):
    repeat 4:
        forward(seite)
        right(90)
        
def folge_von_quadraten(seite, anzahl):
    repeat anzahl:
        quadrat(seite)
        penUp()
        right(90)
        forward(seite)
        left(90)
        penDown()
        seite *= 2
        
       
makeTurtle()
hideTurtle()
folge_von_quadraten(4, 5)

