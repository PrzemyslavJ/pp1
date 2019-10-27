tab = [15,8,31,47,2,19]

i = 0
s = 0
for x in tab:
    if (x % 2 != 0):
        s += x
        i += 1
srednia =  s/i
print(f'Średnia arytmetyczna liczb nieparzystych wynosi: {srednia}')
