def podatek(dochod):
    if dochod<=5000:
        return 0.17*dochod
    else:
        return 0.32*(dochod-5000)+0.17*5000

Pension = float(input("Podaj dochód: "))
print("Podatek należny: ",podatek(Pension))
