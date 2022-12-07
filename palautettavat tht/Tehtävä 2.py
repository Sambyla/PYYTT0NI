from tkinter import X


class henkilo:
    etunimi= ""
    sukunimi= ""
    osoite= ""
    ammatti= ""

def tayta_alkutiedot(alkulista):
    uusi = henkilo()
    uusi.etunimi = "Roope"
    uusi.sukunimi = "Ankka"
    uusi.osoite ="Rahasäiliötie 1"
    uusi.ammatti = "Miljardööri"
    alkulista.append(uusi)
    uusi = henkilo()
    uusi.etunimi = "Aku"
    uusi.sukunimi = "Ankka"
    uusi.osoite ="Paratiisitie 13"
    uusi.ammatti = "Joutilas"
    alkulista.append(uusi)
    uusi = henkilo()
    uusi.etunimi = "Kalle"
    uusi.sukunimi = "Ankka"
    uusi.osoite ="Börjekuja 1"
    uusi.ammatti = "Kenraali"
    alkulista.append(uusi)
    uusi = henkilo()
    uusi.etunimi = "Hessu"
    uusi.sukunimi = "Hopo"
    uusi.osoite ="Neropattikuja 1"
    uusi.ammatti = "Apumies"
    alkulista.append(uusi)
    uusi = henkilo()
    uusi.etunimi = "Polle"
    uusi.sukunimi = "Konikaulus"
    uusi.osoite ="Pollekuja 20"
    uusi.ammatti = "Apulainen"
    alkulista.append(uusi)
    uusi = henkilo()
    uusi.etunimi = "Milla"
    uusi.sukunimi = "Magia"
    uusi.osoite ="Kyöpelinvuori 1"
    uusi.ammatti = "Noita"
    alkulista.append(uusi)

    return alkulista

def lisaa_uusi(a):
    uusi=henkilo()

    uusi.etunimi = input("Etunimi?: ")
    uusi.sukunimi = input("Sukunimi?: ")
    uusi.osoite =input("Osoite?: ")
    uusi.ammatti = input("Ammatti?: ")
    a.append(uusi)
    return a
    
def tulosta_lista_allekkain(a):
    for x in a:
        print
        print("Etunimi:  "+x.etunimi)
        print("Sukunimi: "+x.sukunimi)
        print("Osoite:   "+x.osoite)
        print("Ammatti:  "+x.ammatti)
        print("") 

def tulosta_lista_riveittain(a):
    print("     {:<8s} {:<11s} {:<18s} {:<8}".format("Etunimi", "Sukunimi", "Osoite", "Ammatti"))
    print("     {:<8s} {:<11s} {:<18s} {:<8}".format("*******", "********", "******", "*******"))
    z = 1
    for x in a:
        print("{:>3d}: {:<8} {:<11s} {:<18s} {:<8}".format(z,x.etunimi,x.sukunimi,x.osoite,x.ammatti))
        z+=1
    print("")

def jarjesta_lista_etunimi(a):
    a.sort(key=lambda x: x.etunimi.lower())
    tulosta_lista_riveittain(a)
    return a
    
def jarjesta_lista_sukunimi(a):
    a.sort(key=lambda x: x.sukunimi.lower())
    tulosta_lista_riveittain(a)
    return a

def poista_henkilo(a):
    while True:
        tulosta_lista_riveittain(a)
        p=int(input("Mikä rivi:"))
        x=a[p-1]
        print("{:>3d}: {:<8} {:<11s} {:<18s} {:<8}".format(p,x.etunimi,x.sukunimi,x.osoite,x.ammatti))
        print("Oletko varma? ")
        y=str(input("yes or no:  "))
        if y=="yes":
            a.pop(p-1)
            break
        elif y=="no":
            break
        else:
            print("error. Please try again")

def muuta_henkilotietoja(a):
    while True:
        tulosta_lista_riveittain(a)
        p=int(input("Mikä rivi:"))
        x=a[p-1]
        print("{:>3d}: {:<8s} {:<11s} {:<18s} {:<8s}".format(p,x.etunimi,x.sukunimi,x.osoite,x.ammatti))
        print("Oletko varma? ")
        y=str(input("yes or no:  "))
        if y=="yes":
            a.pop(p-1)
            lisaa_uusi(a)
            break
        elif y=="no":
            break
        else:
            print("error. Please try again")

def haku(a):
    nimi=input("anna hakusana: ")
    rivi=1
    print()
    tulosta_lista_riveittain
    print()
    nimi=nimi.lower()
    for i in a:
        if nimi in i.etunimi.lower() or i.sukunimi.lower() or i.ammatti.lower() or i.osoite.lower():
            print("{:>3d}: {:<8s} {:<11s} {:<18s} {:<8s}".format(rivi,i.etunimi,i.sukunimi,i.osoite,i.ammatti))    
        rivi+=1
def valikko():
    print("")
    print("1. Lisää")
    print("2. Listaa allekkain")
    print("3. Listaa riveittäin")
    print("4. Järjestä etunimen mukaan")
    print("5. Järjestä sukunimen mukaan")
    print("6. Poista henkilö")
    print("7. Muuta henkilöntietoja")
    print("8. Haku")
    print("9. Lopeta")
    print("")
    vastaus=int(input("Vastaus: "))
    return vastaus

def paavalikko():   
    lista = []    
    lista = tayta_alkutiedot(lista)
    while True:    
        valinta = valikko()       
        if valinta == 1:            
            lista = lisaa_uusi(lista)          
        elif valinta == 2:            
            tulosta_lista_allekkain(lista)        
        elif valinta == 3:            
            tulosta_lista_riveittain(lista)        
        elif valinta == 4:            
            lista = jarjesta_lista_etunimi(lista)        
        elif valinta == 5:            
            lista = jarjesta_lista_sukunimi(lista)        
        elif valinta == 6:            
            poista_henkilo(lista)
        elif valinta == 7:
            lista = muuta_henkilotietoja(lista)
        elif valinta == 8:
            lista = haku(lista)           
        else:            
            print()            
            print()            
            break
paavalikko() 

