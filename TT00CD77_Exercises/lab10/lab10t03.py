class Account:
    owner = ""
    saldo = 0
    def __str__(self):
            return self.owner + " " + self.saldo
    def __init__(self, owner = "", saldo = 0):
        self.owner = owner
        self.saldo = saldo

apina = Account()
apina.owner = "Matias Möttönen"
apina.saldo = len(apina.owner)*100

def add(apina, money):
    apina.saldo +=money

def withdraw(apina, money):
    apina.saldo -=money

def accounthandler():
    print("Welcome to the account handler.")
    while True:
        print(f"Bank account created for {apina.owner}.")
        print(f"Bank account balance: {apina.saldo}€.")
        x=int(input("What do you want to do?\nPress following to select:\n1. Add money\n2. Withdraw money\n"))
        if x == 1:
            money=int(input("How many euros will be added? "))
            add(apina, money)
        elif x == 2:
            money=int(input("How many euros will be withdrawn? "))
            if money > apina.saldo:
                print(f"Sorry, you have only {apina.saldo}, the withdraw cannot be done.")
            else:
                withdraw(apina, money)
        else:
            print("Wrong input, try again.")
accounthandler()
