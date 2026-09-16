num1 = int(input(f"Give the first number: "))
num2 = int(input(f"Give the second number: "))
num3 = int(input(f"Give the third number: "))
def average(num1, num2, num3):
    answer= (num1 + num2 + num3) / 3
    final = round(answer, 1)
    return "The average of "+str(num1)+", "+str(num2)+", "+str(num3)+"  is: " + str(final)

print(average(num1, num2, num3))