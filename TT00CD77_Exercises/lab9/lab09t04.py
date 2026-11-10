filename="nimet.txt"
list={}
many=0
with open(filename) as f:
        for x in f:
            x=f.readline()
            many+=1
            if x != "":
                if x in list:
                    list[x]+=1   
                elif x not in list:
                    x=x[:-1] ##otin sen viimeisen \n pois
                    list[x]=1
        
print(f"löytyi: {many} nimeä!") 
oprint = list.items() 
print(f"nimet : {oprint}") 
print(f"monta : {len(list)}") 
