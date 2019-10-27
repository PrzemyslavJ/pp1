import sys
i = 6
j = 1

print("Tablica przy użyciu pętli while")
while i>-1:
    while j<4:
        sys.stdout.write(str(i+j))
        sys.stdout.write(" ")
        j+=1
    i-=3
    j=1
    print("")
        
