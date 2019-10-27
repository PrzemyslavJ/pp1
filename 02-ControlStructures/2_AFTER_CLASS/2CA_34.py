try:
    pesel = str(input("wprowadź numer pesel: "))
    DataUr = pesel[0]+pesel[1]
    wiek = 2018 - (int(DataUr)+1900)
    print("wiek osoby w 2018 roku wynosi: ",wiek)
    if(int(pesel[9])%2==0 or pesel[9]==0):
        print("płęć: Kobieta")
    else:
        print("płeć: Mężczyzna")
except:
    print("Wprowadź poprawny numer pesel!")
