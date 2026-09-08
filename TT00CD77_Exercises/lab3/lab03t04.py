num = int(input("How many points did you get?: "))
if num <= 1 and num >= 0:
    print(f"With your points of: {num}. Your grade is 0. What an unlucky day :c")
elif num >= 2 and num <= 3:
    print(f"With your points of: {num}. Your grade is 1. ouch")
elif num >= 4 and num <= 5:
    print(f"With your points of: {num}. Your grade is 2. Comon you can do better than that :/")
elif num >= 6 and num <= 7:
    print(f"With your points of: {num}. Your grade is 3. Not bad c:")
elif num >= 8 and num <= 9:
    print(f"With your points of: {num}. Your grade is 4. Nice! :)")
elif num >= 10 and num <= 12:
    print(f"With your points of: {num}. Your grade is 5. Congratulations! :D")
else:
    print(f"{num}? That isint on the grade table >:c")