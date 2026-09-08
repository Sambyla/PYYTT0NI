sum = int(0)
count = int(1)
num = int(0)
while count != 6:
    num = int(input(f"{count}.  Give me a number: "))
    if num < 0:
        count += 1
    elif num > 0:
        sum += num
        count += 1
else:
    print(f"The sum is {sum}")