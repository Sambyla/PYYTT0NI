luku=int(input("Anna luku: "))
kerrottava=1
while kerrottava <= luku:
    kertoja=1
    while kertoja <= luku:
        print(f"{kerrottava} x {kertoja} = {kerrottava*kertoja}")
        kertoja +=1
    kerrottava+=1