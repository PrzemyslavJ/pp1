import collections
tab = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]
tab.sort()

def Mediana(tab):
    if(len(tab)% 2 == 0):
        mediana = (tab[int(len(tab)/2)] + tab[int(len(tab)/2 + 1)])/2
    else:
        mediana = tab[int(len(tab)/2)]
    
    return mediana

def Dominanta(tab):
    dom = max(set(tab),key=tab.count)
    return dom

print(list(tab))
print(Mediana(tab))
print(Dominanta(tab))
