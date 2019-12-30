import math
def czytajWspolczynniki():
    tab = []
    a = float(input("Wprowadź współczynnik a: "))
    b = float(input("Wprowadź współczynnik b: "))
    c = float(input("Wprowadź współczynnik c: "))
    tab.append(a)
    tab.append(b)
    tab.append(c)
    return tab

def obliczDelte(wsp):
    a = wsp[0] 
    b = wsp[1] 
    c = wsp[2] 
    return b**2-4*a*c

def wyznaczPierwiastki(delta,wsp):
    a = wsp[0] 
    b = wsp[1] 
    c = wsp[2]
    
    if delta<0:
        return []
    elif delta==0:
        x = -b /(2*a)
        return [x]
    elif delta>0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        return [x1,x2]

def wyswietlpierwiastki(tab):
    if(tab==[]):
        print("równanie nie ma rozwiązania")
    else:
        for i in tab:
            print("Pierwiastek: ",i)
        
    
