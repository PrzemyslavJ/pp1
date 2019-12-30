tabl = [15,38,7,23,14]
def wystepuje(liczba,tablica):
    Cout = 0
    for x in tablica:
        if(liczba==x):
            Cout+=1

    if(Cout==1):
        print("Rezultat: Podana liczba występuje w tablicy")
    else:
        print("Rezultat: Podana liczba nie występuje w tablicy")

liczb = int(input("Wprowadź liczbę: "))
print("liczba:",liczb)
print("tablica:",end=' ')
for i in tabl:
    print(i,end=' ')
print(end='\n')
wystepuje(liczb,tabl)

              
    



       
        
    
    
