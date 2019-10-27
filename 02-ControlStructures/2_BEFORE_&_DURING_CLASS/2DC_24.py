imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]

temp = 0
index = None
for i in imiona:
    if len(i) > temp:
        temp = len(i)
        index = imiona.index(i)
print(f'Najdłuższe imię w tablicy to {imiona[index]}')    
