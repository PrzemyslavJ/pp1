import random
def rzucKostka():
    TablicaLiczb = []
    for x in range(3):
        TablicaLiczb.append(random.randint(1,6))
    return TablicaLiczb

def Sum(tablica):
    suma = 0
    for i in tablica:
        suma+=i
    return suma

x = rzucKostka()
print("Rzuty kostką:",end=' ')
for i in x:
    print(i,end=' ')
print(end='\n')
print("Suma oczek wyrzuconych: ",Sum(x))



    
