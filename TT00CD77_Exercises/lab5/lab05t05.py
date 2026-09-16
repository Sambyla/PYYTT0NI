km = float(input(f"Give the driven amount of km: "))
ltr = float(input(f"Give the average spending per km: "))
cost = float(input(f"Give the price of gas with: "))
def get_cost(km, ltr,cost):
    amount= (ltr * km)/100
    answer= (amount * cost)
    final = round(answer, 2)
    return "The estimate of spent gas in euro is: " + str(final) + "€"

print(get_cost(km, ltr, cost))