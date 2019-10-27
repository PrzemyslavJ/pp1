import sys,random
tab = ["PN","WT","SR","CZ","PI","SB","ND"]
nrDniaTygodnia = random.randint(0,6)
tabTyd = []
a = 0

for i in range(1,31):
    tabTyd.append(i)

print("Kalendarz:")
for i in range(6):
    sys.stdout.write("| ")
    for j in range(7):
        if(i==0):
            sys.stdout.write(tab[j])
            sys.stdout.write(" | ")
        elif(i==1):
            if(j>=nrDniaTygodnia):
                sys.stdout.write(" ")
                sys.stdout.write(str(tabTyd[a]))
                sys.stdout.write(" | ")
                a+=1
            else:
                sys.stdout.write("  ")
                sys.stdout.write(" | ")
        else:
            if(a<30):
                if(tabTyd[a]<10):
                    sys.stdout.write(" ")
                sys.stdout.write(str(tabTyd[a]))
                a+=1
            else:
                sys.stdout.write("  ")
            sys.stdout.write(" | ") 
    print("")

