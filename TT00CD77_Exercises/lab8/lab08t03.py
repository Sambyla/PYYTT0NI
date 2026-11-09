arvosanat=[]
while True:
        tmp=input("Anna Ensimmäisen kurssin arvosana:")
        if tmp == "":
            break
        x= int(tmp)
        if x >= 0 and x <= 5:
            arvosanat.append(x)
        else:
             print("Väärä syöte, yritä uudestaan")
määrä = sum(arvosanat)
pituus = len(arvosanat)
print(f"arvosanojen määrä: {pituus}")
print(f"arvosanojen keskiarvo: {määrä / pituus}")