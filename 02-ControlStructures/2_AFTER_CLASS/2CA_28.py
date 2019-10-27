import sys
a = int(input("Podaj wymiar pionowy a: "))
b = int(input("Podaj wymiar poziomy b: "))

for x in range(a):
        for y in range(b):
            if((x>0 and x <a-1) and (y>0 and y<b-1)):
                sys.stdout.write(" ")
            else:
                sys.stdout.write("*")
        print("")
