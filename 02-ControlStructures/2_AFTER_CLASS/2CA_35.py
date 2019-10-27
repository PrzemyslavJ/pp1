import math
try:
    a=float(input("Wprowadź wspolcznynnik a: "))
    b=float(input("Wprowadź wspolcznynnik b: "))
    c=float(input("Wprowadź wspolcznynnik c: "))
    delta = b**2-4*a*c
  
    if(delta<0):
        print("Równanie nie ma pierwiastków!")
    else:
        if(delta==0):
            x1 = -b/2*a
            print("Równanie ma 1 pierwiastek {:.2f}".format(x1))
        else:
            x1 = (-b-math.sqrt(delta))/2*a
            x2 = (-b+math.sqrt(delta))/2*a
            print("Równanie ma 2 pierwiastki {:.2f}  i {:.2f}".format(x1,x2))
except:
    print("Wprowadź poprawne wartości współczynników !")
