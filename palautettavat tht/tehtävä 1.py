def tulosta_lista(a):
    print(a)

def Lisaa(a):
    nimi=input("mikä nimi?")
    a.append(nimi)

def poista(a):
	print(a)
	#tyhjä muuttuja
	z=0
	for x in a:
		print(f"{z}-{x}")
		z+=1
	poistettava=int(input("Mikä?"))
	a.pop(poistettava)
def paavalikko():
	lista=["Banaani","Päärynä"]
	while True:
		print("PÄÄVALIKKO")
		print("1: Tulosta listan alkiot")
		print("2: Lisää uusi nimi listaan")
		print("3: Poista nimi")
		print("4: Järjestä nimi")
		print("9: Poistu")
		valinta = int(input("Valinta: "))
		if valinta ==9:
			break
		elif valinta ==1:
			tulosta_lista(lista)
		elif valinta ==2:
			Lisaa(lista)
		elif valinta ==3:
			poista(lista)
		elif valinta ==4:
			jarjesta(lista)
paavalikko()
