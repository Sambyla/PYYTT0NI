# def showtime(inp):
#     hours=float(00)
#     minutes=float(00)
#     if inp>=3600: #if seconds are less than an hour first two zeros can be skipped
#         hours=((inp/60)/60)
#         whole=int(hours) #i will seperate the floats halves
#         hdeci=hours-whole
#     elif inp >=60:
#         if hdeci:
            
#         mins=inp/60 Dont think too hard stupid
def showtime(inp):
    tunnit = inp // 3600
    minuutit = (inp % 3600) // 60
    sekunnit = inp % 60

    return f"{tunnit:02}:{minuutit:02}:{sekunnit:02}"

print(showtime(500))
print(showtime(10000))
print(showtime(121000))