import random
Wyniki = []
WynikiPar = []
WynikiNPar = []

def Los():
    return random.randint(1,50)

for i in range(1000):
    Wyniki.append(Los())

for i in Wyniki:
    if(i%2==0):
        WynikiPar.append(i)
    else:
        WynikiNPar.append(i)

print("Dla 1000 liczb losowych z przedziału <1,50>")
print("Liczby parzyste: {:.2f} %".format(len(WynikiPar)/len(Wyniki)*100))
print("Liczby nieparzyste: {:.2f} %".format(len(WynikiNPar)/len(Wyniki)*100))
        
