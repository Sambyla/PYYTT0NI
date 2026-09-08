sum = int(0)
num = int(0)
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekdays:
    num = int(input(f"What is the amount of rain in {day}: "))
    if num < 0:
        print("You can't have negative rain")
    elif num > 0:
        sum += num
else:
    print(f"The sum amount of rain in a week is {sum}")