filename="sukunimet.txt"
while True:
    try:
        x=input("Anna Sukunimi:")
        if x == "":
            break
        file=open(filename,"a")#"a" on sama kun append kun w taas ylikirjoittaa
        file.write(f"{x}, ") ##\n vaihtaa linen
    except:
        print("Tiedoston: " + filename + "lukeminen epäonnistui")
    finally:
        file.close()
print("Homma hoidettu")
