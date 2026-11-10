list=()
with open("sukunimet.txt") as f:
        line=f.read()
        if line != "":
            line=line[:-2] #poistetaan kaksi viimeistä
            list= line.rsplit(", ")
list.sort()
final= ", ".join(list)
print(f"sukunimet aakkosjärjestyksessä: {final}")
