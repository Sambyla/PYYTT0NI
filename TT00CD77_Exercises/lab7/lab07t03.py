#Kuuluisiko tämän olevan input???
class Cat:
    name=str()
    color=str()
    miau=str()
    def __str__(self):
        return self.name + " " + self.color + " " + self.miau
    def __init__(self, name = "", color = "", miau="Meeaaaaow!"):
        self.name = name
        self.color = color
        self.miau= miau
Cat1 = Cat("Kit", "black")
Cat2 = Cat("Kat", "white")
print(f"{Cat1.name}, color: {Cat1.color}")
print(f"{Cat2.name}, color: {Cat2.color}")
print(f"{Cat1.name} says: {Cat1.miau}")
print(f"{Cat2.name} says: {Cat2.miau}")