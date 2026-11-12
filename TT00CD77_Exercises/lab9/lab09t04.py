import os
filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "nimet.txt"
)
list={}
many=0
with open(filename) as f:
        for x in f:
            many+=1
            x=x.strip()#tämä lukee ja ottaa sen muuttujaan kun readline tekisi kahdesti 
            if x in list:
                list[x]+=1
            else:
                 list[x]=1
        # for x in f:
        #     x=f.readline()
        #     many+=1
        #     if x != "":
        #         if x in list:
        #             list[x]+=1   
        #         elif x not in list:
        #             x=x[:-1] ##otin sen viimeisen \n pois
        #             list[x]=1
        
print(f"löytyi: {many} nimeä!") 
# print(f"Nimet: {oprint}")
oprint = "\n".join(f"{nimi}: {maara}" for nimi, maara in list.items())#
print(f"nimet : {oprint}") 
print(f"monta : {len(list)}") 
