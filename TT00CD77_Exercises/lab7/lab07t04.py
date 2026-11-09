#Kuuluisiko tämän olevan input???
class Mobile:
    brand=str()
    model=str()
    price=int()
    def __str__(self):
        return self.brand + " " + self.model + " " + self.price
    def __init__(self, brand = "", model = "", price=0):
        self.brand = brand
        self.model = model
        self.price= price
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(f"Brand: {phone1.brand}, Model: {phone1.model}, Price: {phone1.price}")
print(f"Brand: {phone2.brand}, Model: {phone2.model}, Price: {phone2.price}")
