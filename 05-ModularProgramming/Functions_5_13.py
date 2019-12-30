def slowoOds(word):
    slowoOds = []
    for i in word:
        slowoOds.append(i)
        slowoOds.append(" ")

    return slowoOds

def slowoWspak(word):
    slowoWspak = []
    for i in range(len(word)-1,-1,-1):
        slowoWspak.append(word[i])

    return slowoWspak

def ModSlowo(word):
    NewWord = []
    for i in range(len(word)):
        if(i==0):
            NewWord.append(word[i].upper())
        elif(word[i-1]==" " and word[i] !=" "):
            NewWord.append(word[i].upper())
        else:
            NewWord.append(word[i].lower())

    return NewWord
