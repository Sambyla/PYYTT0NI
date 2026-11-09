kilvet=[]
while True:
        x=input(f"Anna rekisrterikilpi:")
        if x == "":
                break
        kilvet.append(x)
temp = ", ".join(kilvet)
print(f"Kilvet laittamis järjestyksessä: {temp}")
kilvet.sort()
oprint = ", ".join(kilvet)
print(f"Kilvet aakkosjärjestyksessä: {oprint}")