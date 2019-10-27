import sys,math
liczba = int(input("Wprowadź liczbę w systemie dziesiątkowym: "))
tab = []
while(liczba>0):
    tab.append(liczba%2)
    liczba = math.floor(liczba/2)

print("liczba w systemie dwójkowym")
for i in range(len(tab)-1,-1,-1):
    sys.stdout.write(str(tab[i]))
