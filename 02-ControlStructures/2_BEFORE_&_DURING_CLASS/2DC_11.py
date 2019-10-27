login = 'marek'
password = 'm-123'

user_l = input('Podaj login: ')
user_p = input('Podaj hasło: ')

if user_l == login and user_p == password:
    print('Zalogowano poprawnie.')
else:
    print('Nieprawidłowe dane.')
