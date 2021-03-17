with open("seen.txt",'r') as line:
    for word in line:
        if 'rain' in word.lower():
            print(word, end='')