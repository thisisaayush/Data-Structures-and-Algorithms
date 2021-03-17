with open('seen.txt','r') as lines:
    line = lines.readlines()#this line object will have everthing in a txt file as list.
for x in line:
    print(x, end='')#it will break list into the txt format.