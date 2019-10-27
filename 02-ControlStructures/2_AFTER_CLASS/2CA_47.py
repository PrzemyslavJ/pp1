import math
liczba = int(input("Podaj kwotę w zł: "))
piec=0
dwa=0
jeden=0

if (liczba >= 5):
    piec = math.floor(liczba/5)
    if(liczba - piec >= 2):
        dwa= math.floor((liczba - piec*5)/2)
        jeden= liczba - piec*5 - dwa*2
    elif(liczba-piec<2):
        dwa=0
        jeden=liczba-piec*5
        
elif (liczba >= 2 and liczba <5):
    piec=0
    dwa= math.floor(liczba/2)
    jeden- liczba - dwa*2
elif(liczba==1):
    piec=0
    dwa=0
    jeden=1

print("Kwota w monetach",liczba)
print("5zł - {} sztuk".format(piec))
print("2zł - {} sztuk".format(dwa))
print("1zł - {} sztuk".format(jeden))
