from gturtle import *

def kreis(umfang):
    repeat 36:
        forward(umfang / 36)
        right(10)
    #umfang = 1000;
        
def muschel(anzahl, umfang):
    repeat anzahl:
        kreis(umfang)
        umfang *= 1.2
        

makeTurtle()
hideTurtle()
muschel(5, 500)