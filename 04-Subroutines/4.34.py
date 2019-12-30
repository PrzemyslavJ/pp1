def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fib(n-1)+fib(n-2)

Nr = int(input("Wprowadź nr ciągu fibonaciego: "))
print("Wyraz",Nr,"Ciągu fibonaciego wynosi: ",fib(Nr))
print("Pierwszych 20 wyrazów ciągu: ",end=' ')
for i in range(21):
    print(fib(i),end=' ')

        
    
    
    
    
    
    
    
