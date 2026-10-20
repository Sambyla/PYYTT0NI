nimet=[]
x="pekka"
while x != "":
    x=input(f"Anna oppilaan nimi: ")
    if x != "":
        nimet.append(x)
    else:
        False
print(f"Oppilaita: {len(nimet)}")
print(", ".join(nimet)) #saadaan kivasti näi