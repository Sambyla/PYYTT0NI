sana=input("Sana:")
merkki=input("Merkki:")

while True:
    arvo=sana.find(merkki)
    if arvo >= 0:
        if len(sana)- arvo >=3:
            av=arvo+3
            print[arvo:av]
        else:
            break
    else:
        break
    sana=sana[arvo+1:]