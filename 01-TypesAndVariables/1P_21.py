try:
    x = float(input("Podaj temperaturę w C: "))
    if (x>0):
        print(f"{x}°C to {(x)+273.15}°K lub {(x)*1.8 + 32}°F")
    elif(x>=-273.15):
        print(f"{x}°C to {273.15+(x)}°K lub {(x)*1.8 + 32}°F")
    elif(x<2-73.15):
        print("Temperatura poniżej 0 bewględnego!")
except:
    print("Wprowadź poprawną wartość!")
