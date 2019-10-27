import sys

print("Program wyświetlający zakładaną tablice liczb")

for x in range(1,10):
	for y in range(1,10):
		if(y <= x):
			sys.stdout.write(str(x))
	print("")
	
