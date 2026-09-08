fnum = input("First number: ") 
snum = input("Second number: ")
tnum = input("Third number: ")
if fnum > snum and fnum > tnum:
    print(f"biggest number is: {fnum}")
elif fnum < snum and snum > tnum:
    print(f"biggest number is: {snum}")
elif tnum > fnum and tnum > snum:
    print(f"biggest number is: {tnum}")
else:
    print("The numbers are equal")
