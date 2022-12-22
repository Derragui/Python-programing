my_file = 'C:/Users/Dell/Documents/py test/GOOG2.csv'

m = []
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline():
        r = []
        i += 1
        if(i==1):
            continue
        print(f'{i}: {line}', end='')
        for c in line.split(','):
            print(c)
            r.append(c)
            #print(type(c))
        m.append(r)
print()


new_file="C:/Users/Dell/Documents/py test/new.csv"
# 'a' - append to end of file
with open(new_file, 'w') as f: 
    change=[str((float(r[4])-float(r[1]))/float(r[1])) for r in m]
    for i in range(len(m)):
        m[i].append(change[i])
    for r in m:
        print(r)
        cells = [str(i) for i in r]
        print(cells)
        f.write('\t'.join(cells)+'\n')

    
  
