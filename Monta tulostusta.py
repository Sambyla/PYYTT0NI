def tulosta_monesti(a,b):
    while b!=0:
        print(a)
        b-=1
if __name__ == "__main__":
    tulosta_monesti("python", 5)
    tulosta_monesti("hei", 5)
    print()
    merkkijono = "Alussa olivat suo, kuokka ja Python"
    kertaa = 3
    tulosta_monesti(merkkijono, kertaa)
