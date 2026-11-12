import os
filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "names.txt"
)
list=[]
pisin=str()

try:
    with open(filename) as f: #ei tarvitse finally koska with open tekee sen automaattisesti
            for x in f:
                x=x.strip()#tämä lukee ja ottaa sen muuttujaan kun readline tekisi kahdesti¨
                if x == "":
                    continue
                else:
                    list.append(x)
                    if len(x) > len(pisin):
                        pisin=x 
    print(f"Nimet luettu")        
    print(f"Nimiä löytyi: {len(list)}.")
    print(f"Pisin nimi on: {pisin}")
except FileNotFoundError:
    print("Tiedostoa ei löydy: " + filename)
except OSError:
    print("Tiedoston: " + filename + " lukeminen epäonnistui")
 


