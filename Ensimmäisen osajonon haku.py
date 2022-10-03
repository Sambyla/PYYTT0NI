mjono=input("Sana: ")
pituus=len(mjono)
merkki=input("Merkki: ")
if merkki in mjono:
    kohta=mjono.find(merkki)
    lop=kohta
    lop+=3
    tar=mjono[kohta:lop]
    if len(tar)>=3:
       print(tar)