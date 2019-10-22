a = int(input('Wprowadź bok a trójkąta: '))
b = int(input('Wprowadź bok b trójkąta: '))
c = int(input('Wprowadź bok c trójkąta: '))
p = 1/2*(a+b+c)
import cmath
S = cmath.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Pole tego trójkąta wynosi: {S}')
