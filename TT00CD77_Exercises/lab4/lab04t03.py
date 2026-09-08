sum = int(0)
count = int(0)
while True:
    num = input(f"{count}. Give me a number: ")
    if num == "":
        break
    num = int(num)
    sum += num
    count += 1

print(f"How many numbers did you give? {count}")
print(f"The sum of the numbers is {sum}")