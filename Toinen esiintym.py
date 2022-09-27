sana = input("Anna sana: ")

merkki = input("Anna merkki: ")

k = len(merkki)

arvo = sana.find(merkki)

if arvo >= 0:

    arvo1 = sana[k+arvo:].find(merkki)

    if arvo1 >= 0:

        print(f"Osajonon toinen esiintymä on kohdassa {arvo1+arvo+k}.")

    else:

        print("Osajono ei esiinny merkkijonossa kahdesti.")

else:

    print("Osajono ei esiinny merkkijonossa kahdesti.")

    # (en ymmärtänyt)