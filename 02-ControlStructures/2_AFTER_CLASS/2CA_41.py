x=-1
tab = []
while(x!=0):
    x = int(input("Wprowadź liczbę: "))
    if(x!=0):
        tab.append(x)

il = len(tab)
suma = sum(tab)
srednia = suma/il

print("REZULTAT(bez końcowego zera): Liczb={},Suma={},Średnia={:.2f}".format(il,suma,srednia))
        
    
