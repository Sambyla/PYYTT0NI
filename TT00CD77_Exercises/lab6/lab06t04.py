points=[]
count=0
while count != 5:
    x=int(input(f"Hypyn pisteet: "))
    if x<1 or x>20:
        print("Pisteesi ei saa olla alle 1 tai yli 20")
    else:
        points.append(x)
        count+=1
points.remove(min(points))
points.remove(max(points))
print(f"Pisteet yhteensä: {sum(points)}")