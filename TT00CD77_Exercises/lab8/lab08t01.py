nimet=[]
cou=int(0)
while cou != 10:
        x=input(f"Anna oppilaan nimi: ")
        nimet.append(x)
        cou += 1
temp = ", ".join(nimet)
print(f"nimet oikeinpäin: {temp}")
nimet.reverse()
oprint = ", ".join(nimet)
print(f"nimet väärinpäin: {oprint}")