lause=input("Anna lause: ")
lause=lause.split()
#spilt poistaa välit ja laittaa riveihin
for x in lause:
    print(x[0])
#joka ikinen asia listassa x printtaa yksitellen jokaisesta lauseesta ensimmäisen kirjaimen