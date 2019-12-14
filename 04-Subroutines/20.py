def power(x,n):
    Power = 0
    if n == 0:
        Power = 0
    elif n == 1:
        Power = x
    elif n > 1:
        Power = x * power(x,n-1)
    return Power

A = int(input("Wprowadź liczbę do potęgi: "))
B = int(input("Wprowadź potęgę: "))
print("Liczba: ",A," do potęgi ",B," wynosi: ",power(A,B))
        
    
        
