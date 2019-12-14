def suma(N):
    count = 0
    for i in range(N):
        count+=i+1
    return count

def sumaRek(N):
    count = 0
    if N == 0:
        count+= 0
    elif N == 1:
        count+= 1
    elif N > 1:
        count+= N + sumaRek(N-1)
    return count
        

A = int(input("Wprowadź liczbę: "))
print("Suma liczb do tej wartości: ",sumaRek(A))
        
