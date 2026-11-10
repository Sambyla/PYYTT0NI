filename="nimet.txt"
list={}
count=0
with open(filename) as f:
        for x in f:
            x=f.readline()
            count+=1
        if x != "":
            if x in list:
                dict(x.count+=1) 
            list=(x:count=1)
        
print(f"löytyi: {count} nimeä!") 
print(f"löytyi: {len(list)} nimeä!") 
