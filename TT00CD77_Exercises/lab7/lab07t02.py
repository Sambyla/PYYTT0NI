#Kuuluisiko tämän olevan input???
class Human:
    name=""
    age=int()
    def __str__(self):
        return self.name + " " + self.age
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
    def str():
        print(f"nimi: {human1.name}, ikä: {human1.age}")
        print(f"nimi: {human2.name}, ikä: {human2.age}")
human1 = Human("Adam", 19)
human2 = Human("Eva", 18)
Human.str()