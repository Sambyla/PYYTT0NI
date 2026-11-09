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
print(f"Kortti nro 1 maa on {kortti1.maa} ja sen arvo on {kortti1.arvo}")
print(f"Kortti nro 2 maa on {kortti2.maa} ja sen arvo on {kortti2.arvo}")
