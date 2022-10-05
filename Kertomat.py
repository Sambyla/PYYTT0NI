while True:
    luku=int(input("Anna luku: "))
    k1=0
    k1+=1
    k2=2
    if luku==3:
        print(f"luvun 3 kertoma on 6")
        break
    if luku<=1:
        print("Kiitos ja moi!")
        break
    while luku>k1:
        k2=k1*k2
        k1+=1
    print(f"luvun {k1} kertoma on {luku}")