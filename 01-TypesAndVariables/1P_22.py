import math
class LessThanOneError(Exception):
    pass

try:
    a = float(input('Podaj a: '))
    if a <= 0:
        raise LessThanOneError
    b = float(input('Podaj b: '))
    if b <= 0:
        raise LessThanOneError
    c = float(input('Podaj c: '))
    if c <= 0:
        raise LessThanOneError

    p = (a + b + c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Pole trójkąta o bokach długości {:g}, {:g}, {:g} wynosi {:.2f}'.format(a,b,c,S))
except ValueError:
    print('Podana wartość jest nieprawidłowa lub taki trójkąt nie istnieje!')
except LessThanOneError:
    print('Bok trójkąta nie może być mniejszy od 0!')
