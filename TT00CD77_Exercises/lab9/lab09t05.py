import random
filename="lotto.txt"
def lotto():
    pallot=[]
    x=7
    while x != 0:
        pallo=(random.randrange(1,40))
        if pallo not in pallot:
            pass
            pallot.append(pallo)
            x-=1
        else:
            continue
    tuble = tuple(pallot)
    file=open(filename,"a")
    file.write(f"{tuble}\n")
    file.close()
x=int(input("Kuinka monta riviä haluat arpoa: "))
for i in range(x):
    lotto()