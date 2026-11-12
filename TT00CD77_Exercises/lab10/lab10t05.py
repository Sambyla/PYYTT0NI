import os
filename = os.path.join("C:\\", "ayho.txt")
lorem = "Lorem ipsum dolor sit amet consectetur adipiscing elit."

try:
    with open(filename, "a") as file:
        file.write(lorem)
    print("Homma hoidettu")

except PermissionError:
    print("Ei oikeuksia kirjoittaa tiedostoon: " + filename)#juuri hakemistoon ei voi kirjoittaa windowsilla ilman admin oikeuksia!

except OSError:
    print("Tiedoston: " + filename + " käsittely epäonnistui")