import datetime
def kerro3(age):
    if age <= 1:
        print("baby")
    elif age <= 13:
        print("child")
    elif age <= 20:
        print("teen")
    elif age <= 65:
        print("adult")
    else:
        print("senior")
x=input("Anna syntymävuotesi: ")
date = datetime.datetime.today()
age = date.year - int(x)
kerro3(age)