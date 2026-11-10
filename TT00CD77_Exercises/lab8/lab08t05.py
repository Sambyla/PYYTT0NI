import random
def lotto():
    pallot=[]
    x=7
    while x != 0:
        pallo=(random.randrange(1,40))
        pallot.append(pallo)
        x-=1
    tuble = tuple(pallot) ##https://www.w3schools.com/python/python_tuples_update.asp  "Convert the tuple into a list to be able to change it:" :DD ku joini ei oikein halunnut inttien kanssa toimia nii tehdää si näi lol
    print(f"pallosi :D {tuble}")
lotto()