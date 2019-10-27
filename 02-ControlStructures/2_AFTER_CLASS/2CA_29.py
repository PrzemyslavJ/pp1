import sys
tab = [15,8,31,47,2,19]
tabR = []
x = len(tab) - 1

print("Tablica początkowa: ")

for y in tab:
    sys.stdout.write(str(y)+" ")

while(x>-1):
    tabR.append(tab[x])
    x-=1

print("")
print("Tablica odwrócona: ")
for x in tabR:
    sys.stdout.write(str(x)+" ")
    
 
