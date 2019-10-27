zakres = int(input("Zdefiniuj zakres szukania liczby: "))
licznik = 0
for i in range(1,zakres):
    if(i%7==0 and i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1):
        licznik+=1
        print("Liczba spełniająca warunki w szukanym przedziale: ",i)

if (licznik == 0):
    print("Nie ma takiej liczby w szukanym przedziale!")
        
    
        
