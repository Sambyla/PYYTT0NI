name=input(str("what is your name? "))
old=input(str("how old are you? "))
if not old.isdigit():##pitäis tehä hyväksymään vain integeerit
    print("error. Please try again")
    exit()
print(f"Hello {name}")
print(f"Youre {old} years old")