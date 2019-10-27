limit=int(input("Podaj limit prędkości: "))
v = int(input("Podaj prędkość pojazdu: "))

if(v > limit and v<=limit+10):
    Mandat = (v-limit)*5
elif(v>limit+10):
    Mandat =10*5 + (v-(limit+10))*15

print("Mandat(zł): ",Mandat)
