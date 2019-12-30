import csv
print("#","SURNAME","NAME","AGE","EMAIL",sep="       ")
print("="*40)
sum = 0
with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)

    
    for row in reader:
        print(row['surname'],row['name'],row['age'],row['email'],sep="       ")

