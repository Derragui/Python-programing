my_file = 'C:/Users/Dell/Documents/GitHub/Python-programing/py test/GOOG2.csv'
#my_file = input("enter path :")
m = []
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline():
        r = []
        i += 1
        if(i==1):
            continue
        for c in line.split(','):
            c=c.strip()
            r.append(c)
            #print(type(c))
        m.append(r)

new_file="C:/Users/Dell/Documents/GitHub/Python-programing/py test/new.csv"
# 'a' - append to end of file
with open(new_file, 'w') as f: 
    change=[str(((float(r[4])-float(r[1]))/float(r[1]))*100) for r in m]
    listc=[]
    listc.append(["Date ","Open ","High ","Low ","Close ","Adj " "Close "," Volume"])
    for i in range(len(m)):
        m[i].append(change[i])
        listc.append(m[i])
        
    for r in listc:
        print(r)
    for r in listc:
        cells = [i for i in r]
        f.write('\t,'.join(cells)+'\n')

    
  
