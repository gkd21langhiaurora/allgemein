from gturtle import *

def kreis(umfang):
    repeat 36:
        forward(umfang / 36)
        right(10)

def muschel(anzahl, umfang):
    abstand = 100/(2*3.14)
    repeat anzahl:
        kreis(umfang)
        
        left(90)
        penUp()
        forward(abstand)
        penDown()
        right(90)    
    
        umfang += 100
        #abstand *= 1.2
        
makeTurtle()
hideTurtle()
muschel(5, 500)