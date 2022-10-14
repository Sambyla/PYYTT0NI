luku=int(input("Anna luku: "))
pari=luku
ero=1
while pari!=ero and ero<pari:
    print(ero)
    ero+=1
    print(pari)
    pari-=1   
if luku%2!=0:
    print(ero)