import string
i=0
#i had an issue with my file my python couldn't find it even tho both where in the same folder so i gave the full route
with open("C:\\Users\Dell\Documents\my_txt_file.txt", "r") as f:
    data=f.read()
    data=data.translate(str.maketrans('', '', string.punctuation))
    data=data.lower()
    lines=data.split()
    for word in lines:
        #not obliged to add this if
        #if not word.isnumeric():
        i+=1
print(f'The number of words in this text file is: {i}')