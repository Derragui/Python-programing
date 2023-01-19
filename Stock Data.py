my_file = 'C:/Users/Dell/Documents/py test/GOOG2.csv'
#my_file = input("Give me a path :")
m = []
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline():
        r = []
        i += 1
        if(i==1):
            continue
        for c in line.split(','):
            r.append(c)
            #print(type(c))
        m.append(r)


new_file="C:/Users/Dell/Documents/py test/new.csv"
# 'a' - append to end of file
with open(new_file, 'w') as f: 
    change=[str(round((float(r[4])-float(r[1]))/float(r[1]),4)) for r in m]
    listc=[]
    listc.append(["Date", "Open", "High" ,"Low" ,"Close" ,"Adj" ,"Close" ,"Volume"])
    for i in range(len(m)):
        m[i].append(change[i])
        listc.append(m[i])
    
    for r in listc:
        cells = [i.strip() for i in r]
        f.write('\t,'.join(cells)+'\n')

