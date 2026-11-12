maatlista=["Pata", "Hertta", "Risti", "Ruutu"] #äläkysy halusin laittaa nämä turhaan listaan :DD
class Pelikortti:
    maa=""
    arvo=int()
    def __str__(self):
        return self.maa + " " + self.arvo
    def __init__(self, maa = "", arvo = 0):
        self.maa = maa
        self.arvo = arvo

kortti1 = Pelikortti(maatlista[0],14)
kortti2 = Pelikortti(maatlista[2],7)
kortti3 = Pelikortti(maatlista[3],8)
kortti4 = Pelikortti(maatlista[1],7)
kortti5 = Pelikortti(maatlista[0],2)
print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)
