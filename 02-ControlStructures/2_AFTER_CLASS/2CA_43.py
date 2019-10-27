try:
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    c = float(input("Podaj trzecią liczbę: "))

    if(a>=b and a>=c):
        if(b>c):
            print("Liczby w kolejności rosnącej: ",c,b,a)
        else:
            print("Liczby w kolejności rosnącej: ",b,c,a)
    elif(b>=a and b>=c):
        if(a>c):
            print("Liczby w kolejności rosnącej: ",c,a,b)
        else:
            print("Liczby w kolejności rosnącej: ",a,c,b)
    elif(c>=a and c>=b):
        if(a>b):
            print("Liczby w kolejności rosnącej: ",b,a,c)
        else:
            print("Liczby w kolejności rosnącej: ",a,b,c)
        
except:
    print("Wprowadź poprawną liczbę !")

