
while True:
    luku = int(input("Anna luku: "))
    if luku <= 0:
        break
    k1 = 1
    k2 = 1
    while k2 <= luku:
        k1 *= k2
        k2 += 1
    print(f"Luvun {luku} kertoma on {k1}")
print("Kiitos ja moi!")