x = 0
licznik = 0

while(x!="0805"):
    x = str(input("Podaj kod PIN "))
    if(x!="0805"):
        print("Wprowadź poprawny numer !")
        licznik+=1
    if(licznik==3):
        print("Karta płatnicza zostaje zablokowana")
        break

if(x=="0805"):
    print("Poprawny numer karty!")
        
    


