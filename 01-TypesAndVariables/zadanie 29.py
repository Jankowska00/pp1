import random

# komputer rzuca kostką do gry

x = random.randint(1,6)

# użytkownik zgaduje ile oczek wyrzucił komputer

y = int(input('Podaj, ile oczek kostki wyrzucił komputer: '))

# podanie użytkownikowi ile oczek wyliczył komputer i czy użytkownik zgadł odpowiedź

z = (x==y)

print(f'Komputer wyrzucił: {x}')
print(f'Zgadłeś: {z}')
