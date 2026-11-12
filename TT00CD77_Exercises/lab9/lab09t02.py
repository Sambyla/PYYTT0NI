
import os
filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sukunimet.txt"
)
list=()
with open(filename) as f:
        line=f.read()
        if line != "":
            line=line[:-2] #poistetaan kaksi viimeistä
            list= line.rsplit(", ")
list.sort()
final= ", ".join(list)
print(f"sukunimet aakkosjärjestyksessä: {final}")
