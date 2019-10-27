try:
    a = float(input("Wprowadź pierwszą liczbę: "))
    b = float(input("Wprowadź drugą liczbę: "))
    c = a/b
    print("Iloraz liczb = {:.2f}".format(c))
except ZeroDivisionError:
    print("Nie dziel przez zero!")
except:
    print("Niepoprawne liczby!")


