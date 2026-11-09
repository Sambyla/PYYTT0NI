kilvet={}##voi???
count=10
while count!=0:
        reknro=input(f"{count}. Anna rekisrterikilpi: ")
        merkki=input(f"{count}. Anna autonmerkki: ")
        kilvet[reknro] = merkki
        count-=1
kilvet = dict(sorted(kilvet.items()))##ottaa sortin automaattisesti kilven mukaan
print(f"Kilvet aakkosjärjestyksessä: {kilvet}")