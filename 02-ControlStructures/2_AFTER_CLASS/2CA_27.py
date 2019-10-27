import sys
print ("program wyświetlający zadany wzór")

for x in range(9):
    for y in range(5):
        if(x<5 and y<=x):
            sys.stdout.write("*")
        if(x>=5 and y<=-x+8):
            sys.stdout.write("*")
    print("")

    
