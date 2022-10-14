luku=int(input("Anna luku: "))
pari=2
ero=1
if luku%2==0:
    pp="yes"
    while pari<luku:
        print(pari)
        pari+=2   
        print(ero)
        ero+=2
    print(pari)
    print(ero)
elif luku%2!=0:
    pp="no"
    while ero<luku:
        print(pari)
        pari+=2
        print(ero)
        ero+=2
    print(ero)
