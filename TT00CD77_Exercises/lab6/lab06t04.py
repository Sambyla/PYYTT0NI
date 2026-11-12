points=[]
count=0
while count != 5:
    x=int(input(f"Hypyn pisteet: "))
    points.append(x)
    count+=1
points.remove(min(points))
points.remove(max(points))
print(f"Pisteet yhteensä: {sum(points)}")