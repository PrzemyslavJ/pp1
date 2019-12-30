import csv,statistics
AgesEmployees = []
AgesEmployeesI = []
with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
       AgesEmployees.append(row['age'])

for i in AgesEmployees:
    AgesEmployeesI.append(int(i))
print("średnia arytmentyczna wieku pracowników: ",statistics.mean(AgesEmployeesI))
print("mediana wieku pracowników: ",statistics.median(AgesEmployeesI))
print("Odchylenie standardowe wieku pracowników: {:.2f}".format(statistics.stdev(AgesEmployeesI)))
