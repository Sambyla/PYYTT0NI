num1 = int(input(f"Give a number that gets subrtacted from: "))
num2 = int(input(f"Give a number that subtracts: "))
def subtract(num1, num2):
    final = num1 - num2
    return "The result of the subtraction is: " + str(num1) + " - " + str(num2) + " = " + str(final)
print(subtract(num1, num2))