import math
count=1
num = int(input(f"give a number between 1 and 10: "))
if num < 1 or num > 10:
    print("number is not between 1 and 10")
while count != num+1:
    print(f"{count}. square is {count*count}")
    count +=1