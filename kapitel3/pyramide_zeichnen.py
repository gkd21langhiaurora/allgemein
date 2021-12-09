breite = 17
#breite = input("Bitte eine ungerade Zahl eingeben")

if 17%2 == 1:
    leerzeichen_pro_seite = (breite-1)//2
    sterne_pro_seite = 1
    repeat (breite-1)/2:
        print(leerzeichen_pro_seite*" " + sterne_pro_seite*"*" + leerzeichen_pro_seite*" ")
        leerzeichen_pro_seite -=1
        sterne_pro_seite +=2
else:
    print("Nur ungerade Anzahlen erlaubt")
