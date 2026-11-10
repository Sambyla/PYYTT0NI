kilvet={"AAA-123":"Volvo",
        "BBB-456":"BMW",
        "CCC-789":"Opel"
        }##valmiita rekisterinumeroja ja autoja
count=10
last1=str()
while count!=0:
        reknro=input(f"{count}. Anna rekisrterikilpi: ")
        if reknro == "":
                break
        else:
                last1=reknro
                merkki=input(f"{count}. Anna autonmerkki: ")
                kilvet[reknro] = merkki
        if last1 != kilvet[last1]:
            count-=1
            last1=None
        else:
                print("Et voi laittaa jo valmiiksi olevaa rekisterinumeroa! Yritä uudelleen.")
kilvet = dict(sorted(kilvet.items()))##ottaa sortin automaattisesti kilven mukaan
print(f"Kilvet ja niiden automerkt aakkosjärjestyksessä: {kilvet}")