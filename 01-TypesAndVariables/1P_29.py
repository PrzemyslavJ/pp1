import random
class NotInRange(Exception):
    pass

x = random.randint(1,6)

try:
    y = int(input('Podaj, ile oczek kostki wyrzucił komputer: '))
    if (y not in range(1,7)):
        raise NotInRange
    print(f'Komputer wyrzucił {x}')
    if y == x:
        print('Zgadłeś !')
    else:
        print('Nie Zgadłeś !')
    
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except NotInRange:
    print('Wprowadzona wartość nie mieści się w zakresie 1-6')
