import sys
print("Kupon totolotka")
for i in range(1,8):
    for j in range(0,7):
        sys.stdout.write(str(i+j*7))
        if(i+j*7<10 and ((i+(j+1)*7)<10)):
            sys.stdout.write("  ")
        else:
            sys.stdout.write(" ")
    print("")
