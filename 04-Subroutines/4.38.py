Word = input("Wprowadź słowo: ")
WielkieLitery = []
for x in Word:
    if(x.isupper()):
        WielkieLitery.append(x)
print("Wielkie litery: ",end='')
print(list(WielkieLitery))
