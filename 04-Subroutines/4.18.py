def silnia(n):
    if n==0 or n==1:
        return 1
    if n > 1:
        return n*silnia(n-1)

liczba = int(input("Wprowadź liczbę: "))
print("Silnia z",liczba,"wynosi: ",silnia(liczba))
