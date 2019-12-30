liczby = [4,3,7,1,3]
def suma(tab):
    SumCount = 0
    for x in tab:
        SumCount+=x
    print("Tablica: ",end=' ')
    for x in tab:
        print(x,end=' ')
    print(end='\n')  
    print("Suma wartości: ",SumCount)

suma(liczby)

    
