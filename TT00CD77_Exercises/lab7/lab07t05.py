#Kuuluisiko tämän olevan input???
class Car:
    brand=str()
    model=str()
    price=int()
    def __str__(self):
        return self.brand + " " + self.model + " " + self.price
    def __init__(self, brand = "", model = "", price=0):
        self.brand = brand
        self.model = model
        self.price= price
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print(f"auto: {car1.brand} {car1.model} {car1.price}")
print(f"auto: {car2.brand} {car2.model} {car2.price}")
print(f"auto: {car3.brand} {car3.model} {car3.price}")
print(f"autonjen hinta yhteensä: {car1.price + car2.price + car3.price}")
