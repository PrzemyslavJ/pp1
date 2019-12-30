NazwyMiesięcy = ["styczeń","luty","marzec","kwiecień","maj","czerwiec",
                "lipiec","sierpień","wrzesień","październik","listopad","grudzień"]

def miesiąc(N):
    return NazwyMiesięcy[N-1]
try:
    N = int(input("Wprowadź numer miesiąca: "))
    if (N<1 or N>12):
        print("Nieprawidłowy numer")
    else:
        print(miesiąc(N))
except:
    print("nieprawidłowy numer")
    
