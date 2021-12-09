
def reis_schachbrett():
    # starten bei 1
    zahl = 1
    
    summe = 0
    
    # für 64 felder
    repeat 64:
        
        # anzahl Reiskörner auf diesem Feld zur Summe hinzuzählen
        summe += zahl
        
        print(zahl)    
    
        # in jeder runde * 2 rechnen
        zahl *=2
        
    print(summe*0.1/1000/1000)
        

reis_schachbrett()
# 64 Felder: 1 2 4 8 ...