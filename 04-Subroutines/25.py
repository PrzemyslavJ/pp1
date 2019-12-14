Imiona = ["Janek","Ania","Wojtek","Zosia"]

def jestImie(imie,imiona):
    Check = 0
    for i in imiona:
        if (imie==i):
            Check+=1
            
    if Check == 1:
        print("Rezultat: imie zawarte jest w wykazie imion")
    else:
        print("Rezultat: imie nie jest zawarte w wykazie imion")

print("Imiona:",end=' ')
for i in Imiona:
    print(i,end = ' ')
print(end='\n')
Imie = input("Wprowadź imie: ")
jestImie(Imie,Imiona)
            
            
            
