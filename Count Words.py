import string
i=0
list=[]
num=[]
#i had an issue with my file my python couldn't find it even tho both where in the same folder so i gave the full route
with open("C:\\Users\Dell\Documents\my_txt_file.txt", "r") as f:
    data=f.read()
    data=data.translate(str.maketrans('', '', string.punctuation))
    data=data.lower()
    lines=data.split()
    for word in lines:
        #not obliged to add this if
        #if not word.isnumeric():
        if not(word in list):
            list.append(word)
            num.append(1)
        else:
            num[list.index(word)]+=1
        i+=1
print('-------------------------------------------')
for x in range(len(list)):
    print(f'Word "{list[x]}"')
    print(f'Number of itteration :{num[x]}')
    print("*****")
    
print('-------------------------------------------')
print(f'The number of words in this text file is: {i}')