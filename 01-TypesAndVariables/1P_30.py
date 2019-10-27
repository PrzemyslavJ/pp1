tab = [12, 6, 4, 9, 3]
for i in tab:
	count = ''
	for x in range(i):
		count += '*'
	print(str(i) + ": " + count + "\n")
