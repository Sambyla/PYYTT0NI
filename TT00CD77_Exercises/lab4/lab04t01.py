start=0
count=1
num = int(input(f"How many fullnumbers are printed?: "))
while num != 0:
    print(f"{count}. number is {10*start}")
    start += 1
    num -= 1
    count +=1