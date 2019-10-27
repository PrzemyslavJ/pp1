import sys
FirstStr = str(input("Wprowadź ciąg znaków: "))
print("Odwrócony ciąg znaków")
for i in range(len(FirstStr)-1,-1,-1):
    sys.stdout.write(FirstStr[i])
