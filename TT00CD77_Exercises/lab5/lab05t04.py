km = float(input(f"Give the driven amount of km: "))
ltr = float(input(f"Give the average spending per km: "))
def get_fuel(km, ltr):
    answer= (ltr * km) / 100
    final = round(answer, 1)
    return "The estimate of spent gas is: " + str(final) + " liters"

print(get_fuel(km, ltr))