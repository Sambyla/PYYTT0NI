def tulosta_lista(a):
    print(a)

def lisaa(a):
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

def jarjesta(a):
	print(a)
	while True:
		print("")
		s=int(input("Miten?"))
		print("")
		print("1 Uusin ensin")
		print("2 Vanhempi ensin")
		if s==1:
			x=sorted(a)
			print(x)
			break
		if s==2:
			x=sorted(a, reverse=True)
			print(x)
			break
		else:
			print("Error with input, please try again...")

def paavalikko():
	lista=["Banaani","Päärynä"]
	while True:
		print("PÄÄVALIKKO")
		print("")
		print("1: Tulosta listan alkiot")
		print("2: Lisää uusi nimi listaan")
		print("3: Poista nimi")
		print("4: Järjestä nimi")
		print("9: Poistu")
		print("")
		valinta = int(input("Valinta: "))
		print("")
		if valinta ==9:
			break
		elif valinta ==1:
			tulosta_lista(lista)
		elif valinta ==2:
			lisaa(lista)
		elif valinta ==3:
			poista(lista)
		elif valinta ==4:
			jarjesta(lista)
paavalikko()
