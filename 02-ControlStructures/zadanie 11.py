#poprawny login i hasło
login_1 = 'marek'
hasło_1 = 'm-123'

#wprowadzenie loginu i hasła
login_2 = str(input('Podaj login: '))
hasło_2 = str(input('Podaj hasło: '))

#sprawdzenie czy dane są zgodne
if (login_1 == login_2) and (hasło_1 == hasło_2):
    print('Podane dane są prawidłowe.')
else:
    print('Podane dane są nieprawidłowe.')