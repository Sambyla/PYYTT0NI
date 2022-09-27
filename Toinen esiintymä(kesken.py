sana=input("Anna merkkijono:")
merkki=input("Anna osajono:")
arvo=sana.find(merkki)
if arvo >=0:
    k=len(sana)+1
    sana= sana[arvo+1:]
    arvo = sana.find(merkki)
    if arvo >=0:
        print(f"Osajonon toinen esiintymä on kohdassa {arvo+k}")
    else:
       print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")