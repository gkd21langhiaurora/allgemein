from gturtle import *

# Einen Kreis mit vorgegebenem Radius zeichnen. Ausgangsposition muss schon auf dem Kreis liegen
def kreis(radius):
    umfang = 2*3.14*radius
    repeat 120:
        forward(umfang/120)
        right(3)

# Die zwei äusseren Kreise zeichnen in rot
def randkreise(radius):
    setPenColor("red")
    setPos(-radius,-4)
    kreis(radius)
    setPos(-radius-10,-4)
    kreis(radius+10)

# Die inneren Kreise mit gewünschter Anzahl zeichnen
def kreise_innen(anzahl, breite):
    setPenColor("black")
    abstand = breite/anzahl
    radius = abstand
    repeat anzahl:
        setPos(-radius,-2)
        setHeading(0)
        kreis(radius)
        radius += abstand

# Die Dekorationskreise ausserhalb zeichnen
def dekokreise(breite):
    setHeading(11)
    repeat 12:
        setPos(0,0)
        right(360/12)
        penUp()
        forward(breite-20)
        penDown()
        kreis(5)

# Ein einzelnes Blatt zeichnen: Die Werte von winkel, radius und right(27), sowie 180-2*winkel wurden ausprobiert
def blatt():
    winkel = 25
    radius = 340
    right(27)
    blatt_haelfte(winkel, radius)
    right(180-2*winkel)
    blatt_haelfte(winkel,radius)

# Das Blatt, das oben gezeichnet wird, besteht aus zwei derartigen Hälften
def blatt_haelfte(winkel, radius):
    umfang = 2*3.14*radius
    strichlaenge = umfang/360*winkel
    repeat winkel:
        forward(strichlaenge/winkel)
        right(1)

# Die zwölf Blumenblätter zeichnen lassen
def blumenblaetter(innenradius):
    winkel = -30
    repeat 12:
        penUp()
        setPos(0,0)
        setHeading(winkel)
        forward(innenradius)
        penDown()
        blatt()
        winkel += 30
    
        
makeTurtle()
hideTurtle()

# Dies ist die Hälfte der Breite des gesamten Bildes: NICHT VERÄNDERBAR
gesamt_breite = 200

# Die Anzahl der inneren Kreise: VERÄNDERBAR
anzahl_innenkreise = 10

# zwei äussere Kreise als Rand
randkreise(gesamt_breite)

# die inneren Kreise: die Anzahl ist veränderlich
kreise_innen(anzahl_innenkreise,gesamt_breite/3)

# die Blumenblätter des Mandalas
blumenblaetter(gesamt_breite/3)

# die kleinen Kreise am äusseren Rand
dekokreise(gesamt_breite)
    