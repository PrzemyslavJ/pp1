def Sprawdz(n,x,y):
    if(n>=x and n<=y):
        print("liczba n mieście się w podanym zakresie")
    else:
        print("Liczba n nie mieście się w podanym zakresie")

a = int(input("Wprowadź liczbę pierwszą definiującą zakres: "))
b = int(input("Wprowadź drugą liczbę definiującą zakres: "))
c = int(input("Wprowadź liczbę do sprawdzenia: "))
Sprawdz(c,a,b)
