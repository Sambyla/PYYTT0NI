count=0
while True:
        tmp=input("Anna luku: ")
        if tmp == "":
            break
        x= int(tmp)
        filename="luvut.txt"
        file=open(filename,"a")#"a" on sama kun append kun w taas ylikirjoittaa
        file.write(f"{x}, ") ##\n vaihtaa linen
        count +=1


file.write(f"Syötetty {count} lukua, ")
