zakres = int(input("Zdefiniuj zakres szukania liczb pierwszych: "))
dzielnik = 0
dzielnik2 = 0
for i in range(2,zakres+1):
    for j in range(2,i+1):
        if(i%j==0):
            dzielnik+=1
    if(dzielnik==1):
        print("Liczba pierwsza: ",i)
    dzielnik=0

liczba = int(input("Zdefiniuj liczbe aby sprawdzić czy jest pierwwsza: "))
for i in range(2,liczba+1):
    if(liczba%i==0):
        dzielnik2+=1

if(dzielnik2==1):
    print("liczba {} jest liczbą pierwszą ".format(liczba))
else:
    print("liczba {} nie jest liczbą pierwszą ".format(liczba))
       

    
