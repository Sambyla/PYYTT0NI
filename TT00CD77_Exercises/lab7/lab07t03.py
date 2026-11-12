class Cat:
    name=str()
    color=str()
    def __str__(self):
        return self.name + " " + self.color + " "
    def __init__(self, name = "", color = ""):
        self.name = name
        self.color = color
    def miau(self):
        print(f"{self.name} says: Meeaaaaow!")

cat1 = Cat("Kit", "black")
cat2 = Cat("Kat", "white")
print(f"{cat1.name}, color: {cat1.color}")
print(f"{cat2.name}, color: {cat2.color}")
Cat.miau(cat1)
Cat.miau(cat2)