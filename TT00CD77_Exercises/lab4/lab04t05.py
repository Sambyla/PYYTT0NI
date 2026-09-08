fname=input(str("what is your firstname? "))
lname=input(str("what is your lastname? "))
print("Hello " + fname)
leng=len(lname)
full=""
while leng > 0:
    full += str(lname[leng-1])
    leng-=1
print(f"quirky things: {len(fname)*fname[0]} + {full}")